# DailyReminder
# 🤖 Telegram Reminder Bot

A multilingual Telegram bot for managing reminders with timezone support. This is a portfolio/demo project showcasing bot development capabilities.

## ✨ Features

- 🌍 **Multilingual Support**: English, Russian, and Ukrainian
- ⏰ **Smart Reminders**: Create reminders with specific date and time
- 🌐 **Timezone Management**: Automatic time conversion based on user's timezone
- 📋 **Reminder Management**: View and delete active reminders
- 💾 **Persistent Storage**: JSON-based data storage
- 🎯 **User-Friendly Interface**: Reply and inline keyboards for easy navigation
- 🔔 **Background Notifications**: Automatic reminder delivery at scheduled time

## 📋 Available Commands

- `/start` - Initialize bot and select language
- `/set_reminder` - Create a new reminder
- `/list_reminders` - View all active reminders
- `/language` - Change interface language
- `/timezone` - Change timezone settings
- `/help` - Display help information

## 🏗️ Project Structure
```
reminder_bot/
├── main.py                 # Entry point
├── .env                    # Environment variables (TOKEN)
├── requirements.txt        # Dependencies
├── README.md              # This file
├── bot/
│   ├── config.py          # Configuration loader
│   ├── handlers/          # Command and callback handlers
│   │   ├── start.py       # Start, language, timezone handlers
│   │   └── reminders.py   # Reminder CRUD operations
│   ├── services/          # Background services
│   │   └── scheduler.py   # Reminder notification scheduler
│   ├── states/            # FSM states
│   │   └── reminder.py    # Reminder creation states
│   └── utils/             # Utilities
│       ├── localization.py # Multilingual texts
│       ├── keyboards.py    # Keyboard layouts
│       ├── storage.py      # JSON data management
│       └── timezones.py    # Timezone utilities
└── data/
    └── reminders.json     # User data storage
```

## 🚀 Installation

### Prerequisites

- Python 3.8+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))

### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd reminder_bot
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**

Create `.env` file in the root directory:
```env
BOT_TOKEN=your_telegram_bot_token_here
```

5. **Run the bot**
```bash
python main.py
```

## 📦 Dependencies
```
aiogram==3.22.0          # Telegram Bot framework
aiohttp==3.12.15         # Async HTTP client
python-dotenv==1.1.0     # Environment variables
pytz==2024.1             # Timezone handling
```

## 🎯 Usage Example

1. **Start the bot**: Send `/start` command
2. **Select language**: Choose from English, Russian, or Ukrainian
3. **Set timezone**: Pick your timezone from the list
4. **Create reminder**: 
   - Click "➕ Create Reminder" button or use `/set_reminder`
   - Enter reminder text (e.g., "Call the doctor")
   - Enter date in YYYY-MM-DD format (e.g., "2025-10-30")
   - Enter time in HH:MM format (e.g., "15:30")
5. **Manage reminders**: Use "📋 My Reminders" button or `/list_reminders`
6. **Receive notification**: Bot automatically sends reminder at scheduled time

## 🔧 Technical Details

### Architecture

- **Clean Architecture**: Separation of concerns with handlers, services, and utilities
- **FSM (Finite State Machine)**: Step-by-step reminder creation dialog
- **Async/Await**: Full asynchronous operation using aiogram 3.x
- **Background Tasks**: Continuous reminder checking with asyncio
- **JSON Storage**: Lightweight data persistence (easily upgradeable to PostgreSQL)

### Data Structure
```json
{
  "user_id": {
    "language": "en",
    "timezone": "Europe/London",
    "reminders": [
      {
        "id": 1,
        "text": "Call the doctor",
        "date": "2025-10-30",
        "time": "15:30",
        "datetime": "2025-10-30 15:30",
        "created_at": "2025-10-27 12:00:00",
        "is_sent": false
      }
    ]
  }
}
```

### Timezone Handling

- All reminders are stored in UTC
- User inputs time in their local timezone
- Automatic conversion using pytz library
- Supports 18 popular timezones worldwide

## 🎨 Customization

### Adding New Languages

1. Edit `bot/utils/localization.py`
2. Add new language dictionary to `TEXTS`
3. Update language selection keyboard in `bot/handlers/start.py`

### Adding New Timezones

1. Edit `bot/utils/timezones.py`
2. Add timezone to `TIMEZONES` list
3. Format: `("Timezone/Name", "🌍 Display Name (GMT+X)")`

### Extending Functionality

- **Database Migration**: Replace `storage.py` with SQLAlchemy/PostgreSQL
- **Recurring Reminders**: Add frequency field (daily, weekly, monthly)
- **Reminder Categories**: Add tags and filters
- **Notification Options**: Add sound/silent mode preferences

## ⚠️ Important Notes

- This is a **demonstration/portfolio project**
- Designed to showcase bot development skills
- Not recommended for production without additional security measures
- JSON storage is suitable for small-scale usage (<1000 users)

## 🛠️ Development Workflow

The project was built in 8 stages:

1. Basic structure + `/start` with multilingual info
2. Localization system + `/language` command
3. Reply and inline keyboard implementation
4. Reminder creation with FSM dialog
5. JSON persistent storage
6. Background scheduler for notifications
7. Reminder listing and deletion
8. Timezone support and conversion

## 📝 License

This project is open source and available for portfolio demonstration purposes.

## 👨‍💻 Author

Created as a portfolio project to demonstrate:
- Telegram Bot API expertise
- Python async programming
- Clean code architecture
- Multilingual application development
- State management (FSM)
- Background task scheduling

## 🤝 Contact

Looking for a custom Telegram bot? This project demonstrates the ability to create bots with:
- Multiple languages
- Complex workflows
- Database integration
- Custom features tailored to your needs
