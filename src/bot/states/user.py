from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    static = State()
    add_link_name = State()
    add_link = State()
