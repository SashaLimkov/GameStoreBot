from aiogram import Dispatcher
from aiogram.dispatcher import filters
from aiogram.types import ContentTypes

from bot.data import callback_data as cd
from bot.handlers.user import commands, cleaner, games, subscription, sell_process
from bot.states import UserState


def setup(dp: Dispatcher):
    dp.register_message_handler(
        commands.cmd_start, filters.CommandStart(), state="*", is_private=True
    )
    dp.register_callback_query_handler(
        games.game_menu, cd.MAIN_MENU.filter(user_choice="g"), state=UserState.static
    )
    dp.register_callback_query_handler(
        games.get_instruction, cd.GAME_INSTRUCTION.filter(), state=UserState.static
    )
    dp.register_callback_query_handler(
        subscription.get_instruction,
        cd.SUBS_INSTRUCTION.filter(),
        state=UserState.static,
    )
    dp.register_callback_query_handler(
        subscription.subscriptions_menu,
        cd.MAIN_MENU.filter(user_choice="s"),
        state=UserState.static,
    )
    dp.register_callback_query_handler(
        subscription.get_subs_list, cd.SUBS_MENU.filter(), state=UserState.static
    )
    dp.register_callback_query_handler(
        commands.get_mm, filters.Text("back"), state=UserState.static
    )
    dp.register_message_handler(
        sell_process.wait_for_answer,
        lambda message: "хочу" in message.text.lower()
        or "можно" in message.text.lower()
        or "давай купим" in message.text.lower(),
        state=UserState.static,
    )
    # dp.register_message_handler(
    #     sell_process.wait_for_answer,
    #     lambda message: "пользователь" in message.text.lower(),
    # )
    dp.register_message_handler(
        sell_process.add_user_text_message, state=UserState.wait_until_complete
    )
    dp.register_message_handler(
        sell_process.add_user_photo_message,
        content_types=ContentTypes.PHOTO,
        state=UserState.wait_until_complete,
    )
    dp.register_message_handler(cleaner.clean_s, state="*", is_private=True)
    dp.register_message_handler(cleaner.check, state="*")
