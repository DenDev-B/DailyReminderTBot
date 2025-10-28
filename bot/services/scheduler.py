import asyncio
import logging
from datetime import datetime
from aiogram import Bot
from bot.utils.storage import get_all_pending_reminders, mark_reminder_sent, get_user_language
from bot.utils.localization import get_text

logger = logging.getLogger(__name__)


async def check_and_send_reminders(bot: Bot):
    """Check all pending reminders and send notifications if time has come"""
    try:
        pending_reminders = get_all_pending_reminders()
        current_time = datetime.now()
        
        for user_id, reminder in pending_reminders:
            try:
                # Parse reminder datetime
                reminder_datetime = datetime.strptime(
                    reminder["datetime"], 
                    "%Y-%m-%d %H:%M"
                )
                
                # Check if it's time to send (within current minute)
                if (reminder_datetime.year == current_time.year and
                    reminder_datetime.month == current_time.month and
                    reminder_datetime.day == current_time.day and
                    reminder_datetime.hour == current_time.hour and
                    reminder_datetime.minute == current_time.minute):
                    
                    # Get user language
                    lang = get_user_language(user_id)
                    
                    # Prepare notification message
                    message_text = get_text(lang, "reminder_notification").format(
                        text=reminder["text"],
                        date=reminder["date"],
                        time=reminder["time"]
                    )
                    
                    # Send notification
                    await bot.send_message(
                        chat_id=user_id,
                        text=message_text,
                        parse_mode="HTML"
                    )
                    
                    # Mark reminder as sent
                    mark_reminder_sent(user_id, reminder["id"])
                    
                    logger.info(
                        f"Reminder sent to user {user_id}: '{reminder['text']}' "
                        f"scheduled for {reminder['datetime']}"
                    )
                    
            except Exception as e:
                logger.error(
                    f"Error sending reminder to user {user_id}: {e}",
                    exc_info=True
                )
                
    except Exception as e:
        logger.error(f"Error in check_and_send_reminders: {e}", exc_info=True)


async def reminder_scheduler(bot: Bot):
    """Background task that runs every minute to check reminders"""
    logger.info("Reminder scheduler started")
    
    while True:
        try:
            await check_and_send_reminders(bot)
            
            # Wait for 60 seconds before next check
            await asyncio.sleep(60)
            
        except Exception as e:
            logger.error(f"Error in reminder_scheduler loop: {e}", exc_info=True)
            # Wait before retrying
            await asyncio.sleep(60)