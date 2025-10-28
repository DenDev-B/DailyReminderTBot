from aiogram.fsm.state import State, StatesGroup


class ReminderStates(StatesGroup):
    """FSM states for reminder creation"""
    waiting_for_text = State()
    waiting_for_date = State()
    waiting_for_time = State()