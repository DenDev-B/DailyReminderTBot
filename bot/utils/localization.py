# Add new keys to existing TEXTS dictionary
TEXTS = {
    "en": {
        "start_title": "🤖 Reminder Bot - Demo Version",
        "start_info": (
            "📌 <b>This is a demonstration bot</b>\n\n"
            "This bot showcases:\n"
            "• Multi-language support (EN/RU/UA)\n"
            "• Reminder scheduling system\n"
            "• Timezone handling\n\n"
            "⚠️ <b>Not for production use</b>\n"
            "This is a portfolio project. We can create a similar bot "
            "with your required languages and features!\n\n"
            "Use /help to see available commands."
        ),
        "welcome": "👋 Welcome! Select your language to continue.",
        "language_changed": "✅ Language changed to English",
        "select_language": "🌐 Select your language:",
        "help_title": "📖 <b>Available Commands</b>",
        "help_text": (
            "/start - Start bot and select language\n"
            "/language - Change language\n"
            "/timezone - Change timezone\n"
            "/set_reminder - Create new reminder\n"
            "/list_reminders - View your reminders\n"
            "/help - Show this message"
        ),
        "btn_create_reminder": "➕ Create Reminder",
        "btn_my_reminders": "📋 My Reminders",
        "btn_change_language": "🌐 Change Language",
        "btn_help": "❓ Help",
        "menu_opened": "📱 Main menu opened. Choose an action:",
        "reminder_text_prompt": "📝 Enter the reminder text:\n\nExample: Call the doctor",
        "reminder_date_prompt": "📅 Enter the date (YYYY-MM-DD):\n\nExample: 2025-10-28",
        "reminder_time_prompt": "🕐 Enter the time (HH:MM):\n\nExample: 15:30",
        "reminder_created": "✅ Reminder created!\n\n📝 Text: {text}\n📅 Date: {date}\n🕐 Time: {time}",
        "invalid_date_format": "❌ Invalid date format. Please use YYYY-MM-DD\n\nExample: 2025-10-28",
        "invalid_time_format": "❌ Invalid time format. Please use HH:MM\n\nExample: 15:30",
        "date_in_past": "❌ Date cannot be in the past. Please enter a future date.",
        "reminder_cancelled": "❌ Reminder creation cancelled.",
        "btn_cancel": "🚫 Cancel",
        "reminder_notification": "🔔 <b>Reminder!</b>\n\n📝 {text}\n\n📅 Scheduled for: {date} {time}",
        "your_reminders": "📋 <b>Your active reminders:</b>",
        "no_reminders": "📭 You have no active reminders.\n\nCreate one using /set_reminder or the menu button!",
        "reminder_item": "🔔 <b>#{id}</b>\n📝 {text}\n📅 {date} at {time}",
        "btn_delete": "🗑 Delete",
        "reminder_deleted": "✅ Reminder deleted successfully!",
        "reminder_not_found": "❌ Reminder not found. It may have been already deleted or sent.",
        "confirm_delete": "⚠️ Are you sure you want to delete this reminder?\n\n📝 {text}\n📅 {date} at {time}",
        "btn_confirm_delete": "✅ Yes, delete",
        "btn_cancel_delete": "❌ No, keep it",
        "deletion_cancelled": "✅ Deletion cancelled. Reminder kept.",
         "select_timezone": "🌍 Select your timezone:\n\nThis will be used to send reminders at the correct time for you.",
        "timezone_changed": "✅ Timezone changed to: {timezone}",
        "current_timezone": "🌍 Your current timezone: <b>{timezone}</b>\n\nAll reminders will be sent according to this timezone.",
        "timezone_info": "\n\n💡 You can change it anytime using /timezone",
    },
    "ru": {
        "start_title": "🤖 Бот-Напоминалка - Демо Версия",
        "start_info": (
            "📌 <b>Это демонстрационный бот</b>\n\n"
            "Бот демонстрирует:\n"
            "• Мультиязычность (EN/RU/UA)\n"
            "• Систему напоминаний\n"
            "• Работу с часовыми поясами\n\n"
            "⚠️ <b>Не для продакшн использования</b>\n"
            "Это портфолио-проект. Мы можем создать такой же бот "
            "с нужными языками и функционалом!\n\n"
            "Используйте /help для списка команд."
        ),
        "welcome": "👋 Добро пожаловать! Выберите язык для продолжения.",
        "language_changed": "✅ Язык изменён на Русский",
        "select_language": "🌐 Выберите язык:",
        "help_title": "📖 <b>Доступные команды</b>",
        "help_text": (
            "/start - Запустить бота и выбрать язык\n"
            "/language - Сменить язык\n"
            "/timezone - Сменить часовой пояс\n"
            "/set_reminder - Создать напоминание\n"
            "/list_reminders - Посмотреть напоминания\n"
            "/help - Показать это сообщение"
        ),
        "btn_create_reminder": "➕ Создать напоминание",
        "btn_my_reminders": "📋 Мои напоминания",
        "btn_change_language": "🌐 Сменить язык",
        "btn_help": "❓ Помощь",
        "menu_opened": "📱 Главное меню открыто. Выберите действие:",
           "reminder_text_prompt": "📝 Введите текст напоминания:\n\nПример: Позвонить врачу",
        "reminder_date_prompt": "📅 Введите дату (YYYY-MM-DD):\n\nПример: 2025-10-28",
        "reminder_time_prompt": "🕐 Введите время (HH:MM):\n\nПример: 15:30",
        "reminder_created": "✅ Напоминание создано!\n\n📝 Текст: {text}\n📅 Дата: {date}\n🕐 Время: {time}",
        "invalid_date_format": "❌ Неверный формат даты. Используйте YYYY-MM-DD\n\nПример: 2025-10-28",
        "invalid_time_format": "❌ Неверный формат времени. Используйте HH:MM\n\nПример: 15:30",
        "date_in_past": "❌ Дата не может быть в прошлом. Введите будущую дату.",
        "reminder_cancelled": "❌ Создание напоминания отменено.",
        "btn_cancel": "🚫 Отменить",
        "reminder_notification": "🔔 <b>Напоминание!</b>\n\n📝 {text}\n\n📅 Запланировано на: {date} {time}",
        "your_reminders": "📋 <b>Ваши активные напоминания:</b>",
        "no_reminders": "📭 У вас нет активных напоминаний.\n\nСоздайте напоминание через /set_reminder или кнопку меню!",
        "reminder_item": "🔔 <b>№{id}</b>\n📝 {text}\n📅 {date} в {time}",
        "btn_delete": "🗑 Удалить",
        "reminder_deleted": "✅ Напоминание успешно удалено!",
        "reminder_not_found": "❌ Напоминание не найдено. Возможно, оно уже удалено или отправлено.",
        "confirm_delete": "⚠️ Вы уверены, что хотите удалить это напоминание?\n\n📝 {text}\n📅 {date} в {time}",
        "btn_confirm_delete": "✅ Да, удалить",
        "btn_cancel_delete": "❌ Нет, оставить",
        "deletion_cancelled": "✅ Удаление отменено. Напоминание сохранено.",
        "select_timezone": "🌍 Выберите ваш часовой пояс:\n\nОн будет использоваться для отправки напоминаний в правильное время.",
        "timezone_changed": "✅ Часовой пояс изменён на: {timezone}",
        "current_timezone": "🌍 Ваш текущий часовой пояс: <b>{timezone}</b>\n\nВсе напоминания будут отправлены согласно этому поясу.",
        "timezone_info": "\n\n💡 Вы можете изменить его в любое время через /timezone",
    },
    "ua": {
        "start_title": "🤖 Бот-Нагадувач - Демо Версія",
        "start_info": (
            "📌 <b>Це демонстраційний бот</b>\n\n"
            "Бот демонструє:\n"
            "• Мультимовність (EN/RU/UA)\n"
            "• Систему нагадувань\n"
            "• Роботу з часовими поясами\n\n"
            "⚠️ <b>Не для використання в продакшн</b>\n"
            "Це портфоліо-проект. Ми можемо створити такий же бот "
            "з потрібними мовами та функціоналом!\n\n"
            "Використовуйте /help для списку команд."
        ),
        "welcome": "👋 Вітаємо! Оберіть мову для продовження.",
        "language_changed": "✅ Мову змінено на Українську",
        "select_language": "🌐 Оберіть мову:",
        "help_title": "📖 <b>Доступні команди</b>",
        "help_text": (
            "/start - Запустити бота та обрати мову\n"
            "/language - Змінити мову\n"
            "/timezone - Змінити часовий пояс\n"
            "/set_reminder - Створити нагадування\n"
            "/list_reminders - Переглянути нагадування\n"
            "/help - Показати це повідомлення"
        ),
         "btn_create_reminder": "➕ Створити нагадування",
        "btn_my_reminders": "📋 Мої нагадування",
        "btn_change_language": "🌐 Змінити мову",
        "btn_help": "❓ Допомога",
        "menu_opened": "📱 Головне меню відкрито. Оберіть дію:",
        "reminder_text_prompt": "📝 Введіть текст нагадування:\n\nПриклад: Зателефонувати лікарю",
        "reminder_date_prompt": "📅 Введіть дату (YYYY-MM-DD):\n\nПриклад: 2025-10-28",
        "reminder_time_prompt": "🕐 Введіть час (HH:MM):\n\nПриклад: 15:30",
        "reminder_created": "✅ Нагадування створено!\n\n📝 Текст: {text}\n📅 Дата: {date}\n🕐 Час: {time}",
        "invalid_date_format": "❌ Невірний формат дати. Використовуйте YYYY-MM-DD\n\nПриклад: 2025-10-28",
        "invalid_time_format": "❌ Невірний формат часу. Використовуйте HH:MM\n\nПриклад: 15:30",
        "date_in_past": "❌ Дата не може бути в минулому. Введіть майбутню дату.",
        "reminder_cancelled": "❌ Створення нагадування скасовано.",
        "btn_cancel": "🚫 Скасувати",
        "reminder_notification": "🔔 <b>Нагадування!</b>\n\n📝 {text}\n\n📅 Заплановано на: {date} {time}",
        "your_reminders": "📋 <b>Ваші активні нагадування:</b>",
        "no_reminders": "📭 У вас немає активних нагадувань.\n\nСтворіть нагадування через /set_reminder або кнопку меню!",
        "reminder_item": "🔔 <b>№{id}</b>\n📝 {text}\n📅 {date} о {time}",
        "btn_delete": "🗑 Видалити",
        "reminder_deleted": "✅ Нагадування успішно видалено!",
        "reminder_not_found": "❌ Нагадування не знайдено. Можливо, воно вже видалено або надіслано.",
        "confirm_delete": "⚠️ Ви впевнені, що хочете видалити це нагадування?\n\n📝 {text}\n📅 {date} о {time}",
        "btn_confirm_delete": "✅ Так, видалити",
        "btn_cancel_delete": "❌ Ні, залишити",
        "deletion_cancelled": "✅ Видалення скасовано. Нагадування збережено.",
        "select_timezone": "🌍 Оберіть ваш часовий пояс:\n\nВін буде використовуватися для надсилання нагадувань у правильний час.",
        "timezone_changed": "✅ Часовий пояс змінено на: {timezone}",
        "current_timezone": "🌍 Ваш поточний часовий пояс: <b>{timezone}</b>\n\nВсі нагадування будуть надіслані згідно з цим поясом.",
        "timezone_info": "\n\n💡 Ви можете змінити його в будь-який час через /timezone",
        
    }
}

def get_text(lang: str, key: str) -> str:
    """Get localized text by language and key"""
    return TEXTS.get(lang, TEXTS["en"]).get(key, "Text not found")


def get_user_lang(user_id: int, user_languages: dict = None) -> str:
    """Get user language from storage (backward compatible)"""
    from bot.utils.storage import get_user_language
    return get_user_language(user_id)