from aiogram.types import InlineKeyboardMarkup
from bot.data import dict_data as dd
from bot.data import callback_data as cd

__all__ = [
    "get_main_menu"
]

from bot.utils.button_worker import add_button


async def get_main_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        await add_button(
            text="Ключи к играм",
            cd=cd.MAIN_MENU.new(
                user_choice="g"
            )
        )
    )
    keyboard.add(
        await add_button(
            text="Подписки Game Pass Ultimate",
            cd=cd.MAIN_MENU.new(
                user_choice="s"
            )
        )
    )
    return keyboard

# async def get_games_menu():
#     keyboard = InlineKeyboardMarkup(row_width=1)