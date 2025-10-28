import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from bot.config import TOKEN
from bot.handlers import start, reminders
from bot.services.scheduler import reminder_scheduler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

COMMANDS = {
    "en": [
        BotCommand(command="start", description="🚀 Start bot"),
        BotCommand(command="set_reminder", description="➕ Create reminder"),
        BotCommand(command="list_reminders", description="📋 My reminders"),
        BotCommand(command="language", description="🌐 Change language"),
        BotCommand(command="timezone", description="🌍 Change timezone"),
        BotCommand(command="help", description="❓ Help"),
    ],
    "ru": [
        BotCommand(command="start", description="🚀 Запустить бота"),
        BotCommand(command="set_reminder", description="➕ Создать напоминание"),
        BotCommand(command="list_reminders", description="📋 Мои напоминания"),
        BotCommand(command="language", description="🌐 Сменить язык"),
        BotCommand(command="timezone", description="🌍 Сменить часовой пояс"),
        BotCommand(command="help", description="❓ Помощь"),
    ],
    "ua": [
        BotCommand(command="start", description="🚀 Запустити бота"),
        BotCommand(command="set_reminder", description="➕ Створити нагадування"),
        BotCommand(command="list_reminders", description="📋 Мої нагадування"),
        BotCommand(command="language", description="🌐 Змінити мову"),
        BotCommand(command="timezone", description="🌍 Змінити часовий пояс"),
        BotCommand(command="help", description="❓ Допомога"),
    ]
}
    
async def set_bot_commands(bot: Bot):
    """Set default bot commands (English)"""
    await bot.set_my_commands(COMMANDS["en"], scope=BotCommandScopeDefault())
    logger.info("Bot commands set successfully")
    logger.info("Bot commands set successfully")
        
async def set_user_commands(bot: Bot, user_id: int, lang: str):
    """Set personalized commands for specific user based on their language"""
    commands = COMMANDS.get(lang, COMMANDS["en"])
    await bot.set_my_commands(
        commands, 
        scope=BotCommandScopeChat(chat_id=user_id)
    )
    logger.info(f"Commands set for user {user_id} in language {lang}")
        
async def main():
    """Main bot entry point"""
    # Initialize bot and dispatcher
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
   # Set bot commands (menu)
    await set_bot_commands(bot)
    
    # Register routers
    dp.include_router(start.router)
    dp.include_router(reminders.router)
    
    
    scheduler_task = asyncio.create_task(reminder_scheduler(bot))
    logger.info("Background scheduler task created")
    
    try:
        # Start polling
        logger.info("Bot started")
        await dp.start_polling(bot)
    finally:
        # Cancel scheduler task on shutdown
        scheduler_task.cancel()
        try:
            await scheduler_task
        except asyncio.CancelledError:
            logger.info("Scheduler task cancelled")


if __name__ == "__main__":
    asyncio.run(main())