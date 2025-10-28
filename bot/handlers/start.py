from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot.utils.localization import get_text, get_user_lang
from bot.utils.keyboards import get_main_menu_keyboard
from bot.utils.storage import set_user_language, get_user_timezone, set_user_timezone
from bot.utils.timezones import get_timezone_keyboard_data

router = Router()


def get_language_keyboard() -> InlineKeyboardMarkup:
    """Create inline keyboard for language selection"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="🇺🇦 Українська", callback_data="lang_ua"),
        ]
    ])
    return keyboard


def get_timezone_keyboard() -> InlineKeyboardMarkup:
    """Create inline keyboard for timezone selection"""
    timezones = get_timezone_keyboard_data()
    
    # Create keyboard with 2 timezones per row
    keyboard_buttons = []
    for i in range(0, len(timezones), 2):
        row = []
        for j in range(2):
            if i + j < len(timezones):
                tz_id, tz_name = timezones[i + j]
                row.append(InlineKeyboardButton(
                    text=tz_name,
                    callback_data=f"tz_{tz_id}"
                ))
        keyboard_buttons.append(row)
    
    return InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)


@router.message(Command("start"))
async def cmd_start(message: Message):
    """Handle /start command - show language selection"""
    await message.answer(
        "👋 Welcome! / Добро пожаловать! / Вітаємо!\n\n"
        "Please select your language:",
        reply_markup=get_language_keyboard()
    )


@router.callback_query(F.data.startswith("lang_"))
async def process_language_selection(callback: CallbackQuery):
    """Handle language selection from inline buttons"""
    lang_code = callback.data.split("_")[1]
    user_id = callback.from_user.id
    
    # Store user language in JSON
    set_user_language(user_id, lang_code)
    
    # Show timezone selection
    await callback.message.edit_text(
        get_text(lang_code, "select_timezone"),
        reply_markup=get_timezone_keyboard()
    )
    
    await callback.answer(get_text(lang_code, "language_changed"))


@router.callback_query(F.data.startswith("tz_"))
async def process_timezone_selection(callback: CallbackQuery):
    """Handle timezone selection"""
    timezone = callback.data[3:]  # Remove "tz_" prefix
    user_id = callback.from_user.id
    
    # Store timezone
    set_user_timezone(user_id, timezone)
    
    # Get user language
    lang = get_user_lang(user_id)
    
    # Get localized texts
    title = get_text(lang, "start_title")
    info = get_text(lang, "start_info")
    tz_info = get_text(lang, "timezone_info")
    
    # Send info message
    await callback.message.edit_text(
        f"{title}\n\n{info}{tz_info}",
        parse_mode="HTML"
    )
    
    # Send menu with reply keyboard
    menu_text = get_text(lang, "menu_opened")
    await callback.message.answer(
        menu_text,
        reply_markup=get_main_menu_keyboard(lang)
    )
    
    await callback.answer(
        get_text(lang, "timezone_changed").format(timezone=timezone)
    )


@router.message(Command("language"))
async def cmd_language(message: Message):
    """Handle /language command - allow user to change language"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    
    text = get_text(lang, "select_language")
    await message.answer(text, reply_markup=get_language_keyboard())


@router.message(Command("timezone"))
async def cmd_timezone(message: Message):
    """Handle /timezone command - allow user to change timezone"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    current_tz = get_user_timezone(user_id)
    
    text = get_text(lang, "current_timezone").format(timezone=current_tz)
    text += "\n\n" + get_text(lang, "select_timezone")
    
    await message.answer(
        text,
        reply_markup=get_timezone_keyboard(),
        parse_mode="HTML"
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Handle /help command - show available commands"""
    user_id = message.from_user.id
    lang = get_user_lang(user_id)
    
    title = get_text(lang, "help_title")
    help_text = get_text(lang, "help_text")
    
    await message.answer(
        f"{title}\n\n{help_text}",
        parse_mode="HTML"
    )


# Handlers for reply keyboard buttons
@router.message(F.text.in_([
    "🌐 Change Language", "🌐 Сменить язык", "🌐 Змінити мову"
]))
async def button_change_language(message: Message):
    """Handle 'Change Language' button press"""
    await cmd_language(message)


@router.message(F.text.in_([
    "❓ Help", "❓ Помощь", "❓ Допомога"
]))
async def button_help(message: Message):
    """Handle 'Help' button press"""
    await cmd_help(message)