from aiogram.types import InlineKeyboardMarkup
from bot.data import callback_data as cd
from bot.services.db import admin as admin_db

__all__ = [
    "get_admin_panel",
]

from bot.utils.button_worker import add_button


async def get_admin_panel():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        await add_button(
            text="Добавить список",
            cd="add"
        )
    )
    links = await admin_db.get_all_links()
    if links:
        keyboard.add(
            await add_button(
                text="Просмотреть списки",
                cd="show"
            )
        )
        keyboard.add(
            await add_button(
                text="Изменить списки",
                cd="edit"
            )
        )
    return keyboard
