from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class AnalyticReportStates(StatesGroup):
    value_input = State()
