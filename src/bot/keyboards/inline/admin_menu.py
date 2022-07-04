from aiogram.types import InlineKeyboardMarkup
from bot.data import callback_data as cd
from bot.data import text_data as td
from bot.services.db import admin as admin_db

__all__ = ["get_admin_panel", "get_links_list", "get_links_to_del", "confirm_delete", "consult_quick_menu"]

from bot.utils.button_worker import add_button


async def get_admin_panel():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(await add_button(text="Добавить список", cd="add"))
    links = await admin_db.get_all_links()
    if links:
        keyboard.add(await add_button(text="Просмотреть списки", cd="show"))
        keyboard.add(await add_button(text="Изменить списки", cd="edit"))
    return keyboard


async def get_links_list():
    keyboard = InlineKeyboardMarkup(row_width=1)
    links = await admin_db.get_all_links()
    for link in links:
        keyboard.add(
            await add_button(
                text=link.name,
                url=link.link,
            )
        )
    keyboard.add(await add_button(text=td.BACK_TO_MM, cd=td.BACK_TO_A_MM_CD))
    return keyboard


async def get_links_to_del():
    keyboard = InlineKeyboardMarkup(row_width=2)
    links = await admin_db.get_all_links()
    for link in links:
        keyboard.insert(
            await add_button(
                text=link.name,
                cd=".",
            )
        )
        keyboard.insert(
            await add_button(
                text="🗑",
                cd=f"del_{link.id}",
            )
        )
    keyboard.add(await add_button(text=td.BACK_TO_MM, cd=td.BACK_TO_A_MM_CD))
    return keyboard


async def confirm_delete(link_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(await add_button(text="Подтвердить", cd=f"confirm_{link_id}"))
    keyboard.add(await add_button(text="Отмена", cd="edit"))
    return keyboard


async def consult_quick_menu(u_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(await add_button(text="Привет, оплачивай (игры)", cd=f"send_text_{u_id}"))
    keyboard.add(await add_button(text="Оплата прошла", cd=f"money_success_{u_id}"))
    keyboard.add(await add_button(text="Какой телефон?", cd=f"user_phone_{u_id}"))
    keyboard.add(await add_button(text="🤖🇹🇷", cd=f"and_t_{u_id}"))
    keyboard.insert(await add_button(text="🍏🇹🇷", cd=f"app_t_{u_id}"))
    keyboard.insert(await add_button(text="🤖🇦🇷", cd=f"and_a_{u_id}"))
    keyboard.insert(await add_button(text="🍏🇦🇷", cd=f"app_a_{u_id}"))
    keyboard.add(await add_button(text="Привет, оплачивай (подписки)", cd=f"sub_text_{u_id}"))
    keyboard.add(await add_button(text="🤖", cd=f"subs_app_{u_id}"))
    keyboard.insert(await add_button(text="🍏", cd=f"subs_and_{u_id}"))
    keyboard.add(await add_button(text="Активируй, пиши", cd=f"act_{u_id}"))
    return keyboard
