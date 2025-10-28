from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from bot.utils.localization import get_text


def get_main_menu_keyboard(lang: str) -> ReplyKeyboardMarkup:
    """Create main menu reply keyboard based on user language"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=get_text(lang, "btn_create_reminder")),
                KeyboardButton(text=get_text(lang, "btn_my_reminders"))
            ],
            [
                KeyboardButton(text=get_text(lang, "btn_change_language")),
                KeyboardButton(text=get_text(lang, "btn_help"))
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder=get_text(lang, "select_language") if lang else "Choose action..."
    )
    return keyboard


def get_cancel_keyboard(lang: str) -> ReplyKeyboardMarkup:
    """Create keyboard with cancel button"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_text(lang, "btn_cancel"))]
        ],
        resize_keyboard=True
    )
    return keyboard


def remove_keyboard() -> ReplyKeyboardRemove:
    """Remove keyboard"""
    return ReplyKeyboardRemove()