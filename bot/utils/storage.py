import json
import os
from typing import Dict, List, Optional
from datetime import datetime


DATA_FILE = "data/reminders.json"


def load_data() -> Dict:
    """Load all data from JSON file"""
    if not os.path.exists(DATA_FILE):
        # Create data directory if not exists
        os.makedirs("data", exist_ok=True)
        return {}
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_data(data: Dict) -> None:
    """Save all data to JSON file"""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_user_data(user_id: int) -> Dict:
    """Get user data from storage"""
    data = load_data()
    user_id_str = str(user_id)
    
    if user_id_str not in data:
        # Initialize new user with default values
        data[user_id_str] = {
            "language": "en",
            "timezone": "UTC",  # Will be used in stage 8
            "reminders": []
        }
        save_data(data)
    
    return data[user_id_str]


def set_user_language(user_id: int, language: str) -> None:
    """Set user language preference"""
    data = load_data()
    user_id_str = str(user_id)
    
    if user_id_str not in data:
        data[user_id_str] = {
            "language": language,
            "timezone": "UTC",
            "reminders": []
        }
    else:
        data[user_id_str]["language"] = language
    
    save_data(data)


def get_user_language(user_id: int) -> str:
    """Get user language from storage"""
    user_data = get_user_data(user_id)
    return user_data.get("language", "en")


def add_reminder(user_id: int, text: str, date: str, time: str) -> Dict:
    """Add new reminder for user"""
    data = load_data()
    user_id_str = str(user_id)
    
    # Ensure user data exists
    if user_id_str not in data:
        data[user_id_str] = {
            "language": "en",
            "timezone": "UTC",
            "reminders": []
        }
    
    # Create reminder object
    reminder = {
        "id": len(data[user_id_str]["reminders"]) + 1,  # Simple ID generation
        "text": text,
        "date": date,
        "time": time,
        "datetime": f"{date} {time}",  # Combined for easier sorting
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "is_sent": False
    }
    
    # Add reminder to user's list
    data[user_id_str]["reminders"].append(reminder)
    save_data(data)
    
    return reminder


def get_user_reminders(user_id: int, active_only: bool = True) -> List[Dict]:
    """Get all reminders for user"""
    user_data = get_user_data(user_id)
    reminders = user_data.get("reminders", [])
    
    if active_only:
        # Return only reminders that haven't been sent
        return [r for r in reminders if not r.get("is_sent", False)]
    
    return reminders


def delete_reminder(user_id: int, reminder_id: int) -> bool:
    """Delete reminder by ID"""
    data = load_data()
    user_id_str = str(user_id)
    
    if user_id_str not in data:
        return False
    
    reminders = data[user_id_str]["reminders"]
    initial_length = len(reminders)
    
    # Filter out the reminder with matching ID
    data[user_id_str]["reminders"] = [
        r for r in reminders if r.get("id") != reminder_id
    ]
    
    save_data(data)
    return len(data[user_id_str]["reminders"]) < initial_length


def mark_reminder_sent(user_id: int, reminder_id: int) -> bool:
    """Mark reminder as sent"""
    data = load_data()
    user_id_str = str(user_id)
    
    if user_id_str not in data:
        return False
    
    for reminder in data[user_id_str]["reminders"]:
        if reminder.get("id") == reminder_id:
            reminder["is_sent"] = True
            save_data(data)
            return True
    
    return False


def get_all_pending_reminders() -> List[tuple]:
    """Get all pending reminders from all users (for background task)"""
    data = load_data()
    pending = []
    
    for user_id_str, user_data in data.items():
        for reminder in user_data.get("reminders", []):
            if not reminder.get("is_sent", False):
                pending.append((int(user_id_str), reminder))
    
    return pending

def get_user_timezone(user_id: int) -> str:
    """Get user timezone from storage"""
    user_data = get_user_data(user_id)
    return user_data.get("timezone", "UTC")


def set_user_timezone(user_id: int, timezone: str) -> None:
    """Set user timezone preference"""
    data = load_data()
    user_id_str = str(user_id)
    
    if user_id_str not in data:
        data[user_id_str] = {
            "language": "en",
            "timezone": timezone,
            "reminders": []
        }
    else:
        data[user_id_str]["timezone"] = timezone
    
    save_data(data)