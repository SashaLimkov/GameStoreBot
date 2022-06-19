from aiogram.types import InlineKeyboardMarkup
from bot.data import text_data as td
from bot.data import callback_data as cd
from bot.services.db import user as user_db

__all__ = [
    "get_main_menu",
    "get_games_menu",
    "get_subs_menu",
    "back"
]

from bot.utils.button_worker import add_button


async def get_main_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        await add_button(
            text="Игры",
            cd=cd.MAIN_MENU.new(
                user_choice="g"
            )
        )
    )
    keyboard.add(
        await add_button(
            text="Подписки",
            cd=cd.MAIN_MENU.new(
                user_choice="s"
            )
        )
    )
    return keyboard


async def get_games_menu(callback_data: dict):
    keyboard = InlineKeyboardMarkup(row_width=1)
    links = await user_db.get_all_links()
    for link in links:
        keyboard.add(
            await add_button(
                text=link.name,
                url=link.link,
            )
        )
    keyboard.add(await add_button(
        text=td.GAME_INSTRUCTION,
        cd=cd.GAME_INSTRUCTION.new(
            user_choice=callback_data["user_choice"],
            instruction=1
        )
    ))
    keyboard.add(await add_button(
        text=td.BACK_TO_MM,
        cd=td.BACK_TO_MM_CD
    ))
    return keyboard


async def get_subs_menu(callback_data: dict):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(await add_button(
        text="Список подписок",
        cd=cd.SUBS_MENU.new(
            user_choice=callback_data["user_choice"],
            s_list=1
        )
    ))
    keyboard.add(await add_button(
        text=td.BACK_TO_MM,
        cd=td.BACK_TO_MM_CD
    ))
    return keyboard


async def back(callback_data: dict):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(await add_button(
        text=td.BACK_TO_MM,
        cd=cd.MAIN_MENU.new(
            user_choice=callback_data["user_choice"]
        )
    ))
    return keyboard
