from aiogram import Dispatcher
from aiogram.dispatcher import filters
from bot.data import callback_data as cd
from bot.handlers.user import commands, cleaner, games, subscription
from bot.states import UserState


def setup(dp: Dispatcher):
    dp.register_message_handler(commands.cmd_start, filters.CommandStart(), state="*")
    dp.register_callback_query_handler(games.game_menu, cd.MAIN_MENU.filter(
        user_choice="g"
    ), state=UserState.static)
    dp.register_callback_query_handler(games.get_instruction, cd.GAME_INSTRUCTION.filter(), state="*")
    dp.register_callback_query_handler(subscription.subscriptions_menu, cd.MAIN_MENU.filter(
        user_choice="s"
    ), state=UserState.static)
    dp.register_callback_query_handler(subscription.get_subs_list, cd.SUBS_MENU.filter(), state="*")
    dp.register_callback_query_handler(commands.get_mm, filters.Text("back"), state="*")
    dp.register_message_handler(cleaner.clean_s, state="*")
