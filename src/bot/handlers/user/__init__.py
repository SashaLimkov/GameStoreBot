from aiogram import Dispatcher
from aiogram.dispatcher import filters
from bot.data import callback_data as cd
from bot.handlers.user import commands, cleaner, games
from bot.states import UserState


def setup(dp: Dispatcher):
    dp.register_message_handler(commands.cmd_start, filters.CommandStart(), state="*")
    dp.register_callback_query_handler(games.game_menu, cd.MAIN_MENU.filter(), state=UserState.static)
    dp.register_message_handler(cleaner.clean_s, state="*")
