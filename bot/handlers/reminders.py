from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from datetime import datetime
from bot.states.reminder import ReminderStates
from bot.utils.localization import get_text, get_user_lang
from bot.utils.keyboards import get_cancel_keyboard, get_main_menu_keyboard
from bot.utils.storage import add_reminder, get_user_reminders, delete_reminder, get_user_timezone  # Add new imports
from bot.utils.timezones import convert_to_utc

router = Router()


@router.message(Command("set_reminder"))
async def cmd_set_reminder(message: Message, state: FSMContext):
    """Start reminder creation process"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    
    await state.set_state(ReminderStates.waiting_for_text)
    await message.answer(
        get_text(lang, "reminder_text_prompt"),
        reply_markup=get_cancel_keyboard(lang)
    )


@router.message(F.text.in_(["🚫 Cancel", "🚫 Отменить", "🚫 Скасувати"]))
async def cancel_reminder(message: Message, state: FSMContext):
    """Cancel reminder creation"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    
    await state.clear()
    await message.answer(
        get_text(lang, "reminder_cancelled"),
        reply_markup=get_main_menu_keyboard(lang)
    )


@router.message(ReminderStates.waiting_for_text)
async def process_reminder_text(message: Message, state: FSMContext):
    """Process reminder text input"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    
    # Save reminder text to FSM storage
    await state.update_data(text=message.text)
    
    # Move to next state
    await state.set_state(ReminderStates.waiting_for_date)
    await message.answer(
        get_text(lang, "reminder_date_prompt"),
        reply_markup=get_cancel_keyboard(lang)
    )


@router.message(ReminderStates.waiting_for_date)
async def process_reminder_date(message: Message, state: FSMContext):
    """Process reminder date input"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    
    # Validate date format
    try:
        date_obj = datetime.strptime(message.text, "%Y-%m-%d")
        
        # Check if date is not in the past
        if date_obj.date() < datetime.now().date():
            await message.answer(
                get_text(lang, "date_in_past"),
                reply_markup=get_cancel_keyboard(lang)
            )
            return
        
        # Save date to FSM storage
        await state.update_data(date=message.text)
        
        # Move to next state
        await state.set_state(ReminderStates.waiting_for_time)
        await message.answer(
            get_text(lang, "reminder_time_prompt"),
            reply_markup=get_cancel_keyboard(lang)
        )
        
    except ValueError:
        await message.answer(
            get_text(lang, "invalid_date_format"),
            reply_markup=get_cancel_keyboard(lang)
        )


@router.message(ReminderStates.waiting_for_time)
async def process_reminder_time(message: Message, state: FSMContext):
    """Process reminder time input and create reminder"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    
    # Validate time format
    try:
        time_obj = datetime.strptime(message.text, "%H:%M")
        
        # Get all data from FSM storage
        data = await state.get_data()
        reminder_text = data.get("text")
        reminder_date = data.get("date")
        reminder_time = message.text
        
        # Get user's timezone
        user_tz = get_user_timezone(user_id)
        
        # Convert to UTC for storage
        utc_datetime = convert_to_utc(reminder_date, reminder_time, user_tz)
        
        # Check if datetime is not in the past
        if utc_datetime < datetime.now(pytz.UTC):
            await message.answer(
                get_text(lang, "date_in_past"),
                reply_markup=get_cancel_keyboard(lang)
            )
            return
        
        # Save reminder to JSON (store UTC time)
        reminder = add_reminder(
            user_id, 
            reminder_text, 
            utc_datetime.strftime("%Y-%m-%d"),
            utc_datetime.strftime("%H:%M")
        )
        
        # Clear FSM state
        await state.clear()
        
        # Show confirmation with user's local time
        confirmation = get_text(lang, "reminder_created").format(
            text=reminder_text,
            date=reminder_date,
            time=reminder_time
        )
        
        await message.answer(
            confirmation,
            reply_markup=get_main_menu_keyboard(lang)
        )
        
    except ValueError:
        await message.answer(
            get_text(lang, "invalid_time_format"),
            reply_markup=get_cancel_keyboard(lang)
        )


# Handler for button press (from main menu)
@router.message(F.text.in_([
    "➕ Create Reminder", "➕ Создать напоминание", "➕ Створити нагадування"
]))
async def button_create_reminder(message: Message, state: FSMContext):
    """Handle 'Create Reminder' button press"""
    await cmd_set_reminder(message, state)


@router.message(Command("list_reminders"))
async def cmd_list_reminders(message: Message):
    """Show all active reminders for user"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    
    # Get active reminders
    reminders = get_user_reminders(user_id, active_only=True)
    
    if not reminders:
        await message.answer(get_text(lang, "no_reminders"))
        return
    
    # Sort reminders by datetime
    reminders.sort(key=lambda r: r["datetime"])
    
    # Send header
    await message.answer(get_text(lang, "your_reminders"))
    
    # Send each reminder with delete button
    for reminder in reminders:
        reminder_text = get_text(lang, "reminder_item").format(
            id=reminder["id"],
            text=reminder["text"],
            date=reminder["date"],
            time=reminder["time"]
        )
        
        # Create inline keyboard with delete button
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text=get_text(lang, "btn_delete"),
                callback_data=f"delete_{reminder['id']}"
            )]
        ])
        
        await message.answer(
            reminder_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )


@router.message(F.text.in_([
    "📋 My Reminders", "📋 Мои напоминания", "📋 Мої нагадування"
]))
async def button_list_reminders(message: Message):
    """Handle 'My Reminders' button press"""
    await cmd_list_reminders(message)


@router.callback_query(F.data.startswith("delete_"))
async def process_delete_request(callback: CallbackQuery):
    """Show confirmation dialog for reminder deletion"""
    user_id = callback.from_user.id
    lang = get_user_lang(user_id)
    
    # Extract reminder ID
    reminder_id = int(callback.data.split("_")[1])
    
    # Get reminder details
    reminders = get_user_reminders(user_id, active_only=True)
    reminder = next((r for r in reminders if r["id"] == reminder_id), None)
    
    if not reminder:
        await callback.answer(
            get_text(lang, "reminder_not_found"),
            show_alert=True
        )
        return
    
    # Create confirmation keyboard
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=get_text(lang, "btn_confirm_delete"),
                callback_data=f"confirm_delete_{reminder_id}"
            ),
            InlineKeyboardButton(
                text=get_text(lang, "btn_cancel_delete"),
                callback_data=f"cancel_delete_{reminder_id}"
            )
        ]
    ])
    
    # Show confirmation message
    confirm_text = get_text(lang, "confirm_delete").format(
        text=reminder["text"],
        date=reminder["date"],
        time=reminder["time"]
    )
    
    await callback.message.edit_text(
        confirm_text,
        reply_markup=keyboard
    )
    await callback.answer()


@router.callback_query(F.data.startswith("confirm_delete_"))
async def process_confirm_delete(callback: CallbackQuery):
    """Delete reminder after confirmation"""
    user_id = callback.from_user.id
    lang = get_user_lang(user_id)
    
    # Extract reminder ID
    reminder_id = int(callback.data.split("_")[2])
    
    # Delete reminder
    success = delete_reminder(user_id, reminder_id)
    
    if success:
        await callback.message.edit_text(
            get_text(lang, "reminder_deleted")
        )
    else:
        await callback.message.edit_text(
            get_text(lang, "reminder_not_found")
        )
    
    await callback.answer()


@router.callback_query(F.data.startswith("cancel_delete_"))
async def process_cancel_delete(callback: CallbackQuery):
    """Cancel reminder deletion"""
    user_id = callback.from_user.id
    lang = get_user_lang(user_id)
    
    # Extract reminder ID
    reminder_id = int(callback.data.split("_")[2])
    
    # Get reminder details to restore original message
    reminders = get_user_reminders(user_id, active_only=True)
    reminder = next((r for r in reminders if r["id"] == reminder_id), None)
    
    if reminder:
        reminder_text = get_text(lang, "reminder_item").format(
            id=reminder["id"],
            text=reminder["text"],
            date=reminder["date"],
            time=reminder["time"]
        )
        
        # Restore delete button
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text=get_text(lang, "btn_delete"),
                callback_data=f"delete_{reminder['id']}"
            )]
        ])
        
        await callback.message.edit_text(
            reminder_text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    
    await callback.answer(get_text(lang, "deletion_cancelled"))