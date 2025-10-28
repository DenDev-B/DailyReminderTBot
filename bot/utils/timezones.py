from typing import List, Tuple
from datetime import datetime


# Popular timezones with user-friendly names
TIMEZONES = [
    ("UTC", "🌍 UTC (GMT+0)"),
    ("Europe/London", "🇬🇧 London (GMT+0)"),
    ("Europe/Paris", "🇫🇷 Paris (GMT+1)"),
    ("Europe/Berlin", "🇩🇪 Berlin (GMT+1)"),
    ("Europe/Kiev", "🇺🇦 Kyiv (GMT+2)"),
    ("Europe/Moscow", "🇷🇺 Moscow (GMT+3)"),
    ("Asia/Dubai", "🇦🇪 Dubai (GMT+4)"),
    ("Asia/Karachi", "🇵🇰 Karachi (GMT+5)"),
    ("Asia/Almaty", "🇰🇿 Almaty (GMT+6)"),
    ("Asia/Bangkok", "🇹🇭 Bangkok (GMT+7)"),
    ("Asia/Shanghai", "🇨🇳 Shanghai (GMT+8)"),
    ("Asia/Tokyo", "🇯🇵 Tokyo (GMT+9)"),
    ("Australia/Sydney", "🇦🇺 Sydney (GMT+11)"),
    ("Pacific/Auckland", "🇳🇿 Auckland (GMT+13)"),
    ("America/New_York", "🇺🇸 New York (GMT-5)"),
    ("America/Chicago", "🇺🇸 Chicago (GMT-6)"),
    ("America/Denver", "🇺🇸 Denver (GMT-7)"),
    ("America/Los_Angeles", "🇺🇸 Los Angeles (GMT-8)"),
]


def get_timezone_keyboard_data() -> List[Tuple[str, str]]:
    """Get timezone data for keyboard generation"""
    return TIMEZONES


def convert_to_utc(date_str: str, time_str: str, user_timezone: str) -> datetime:
    """Convert user's local datetime to UTC"""
    try:
        # Parse user's datetime
        local_dt_str = f"{date_str} {time_str}"
        naive_dt = datetime.strptime(local_dt_str, "%Y-%m-%d %H:%M")
        
        # Localize to user's timezone
        user_tz = pytz.timezone(user_timezone)
        local_dt = user_tz.localize(naive_dt)
        
        # Convert to UTC
        utc_dt = local_dt.astimezone(pytz.UTC)
        
        return utc_dt
    except Exception:
        # Fallback to naive datetime if conversion fails
        return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")


def get_user_local_time(utc_datetime: datetime, user_timezone: str) -> datetime:
    """Convert UTC datetime to user's local time"""
    try:
        user_tz = pytz.timezone(user_timezone)
        
        # Ensure UTC datetime is timezone-aware
        if utc_datetime.tzinfo is None:
            utc_datetime = pytz.UTC.localize(utc_datetime)
        
        # Convert to user's timezone
        local_dt = utc_datetime.astimezone(user_tz)
        
        return local_dt
    except Exception:
        return utc_datetime
