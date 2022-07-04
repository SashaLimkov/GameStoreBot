from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToEditNotFound, MessageCantBeEdited
from aiogram.utils.markdown import hlink

from bot.config.loader import bot, user_data
from bot.handlers.admin.commands import admin_panel, send_admin_panel
from bot.states import UserState
from bot.utils import deleter
from bot.services.db import admin as admin_db
from bot.utils.commands_setter import set_default_commands, delete_default_commands
from bot.utils.deleter import delete_user_message
from bot.data import text_data as td
from bot.keyboards import inline as ik
from bot.utils.url_validator import is_url_valid
from store.models import LinkGameList


async def a_p(call: types.CallbackQuery, state: FSMContext):
    await send_admin_panel(message=call.message, state=state)


async def add_link_name(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    mes_to_del = data.get("mes_to_del")
    mes = await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=td.ADD_LINK_NAME,
    )
    mes_to_del = [mes.message_id]
    await UserState.add_link_name.set()
    await state.update_data(mes_to_del=mes_to_del)


async def add_link(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    mes_to_del = data.get("mes_to_del")
    mes = await bot.send_message(chat_id=message.chat.id, text=td.ADD_LINK)
    mes_to_del += [mes.message_id, message.message_id]
    await UserState.add_link.set()
    await state.update_data(mes_to_del=mes_to_del)


async def finish_adding_link(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    link = message.text
    valid = await is_url_valid(link)
    if valid:
        await deleter.delete_user_message(message)
        await deleter.delete_bot_messages(message.chat.id, state)
        await admin_db.add_link(name=name, link=link)
        await admin_panel(message, state)
        await UserState.static.set()
    else:
        mes_to_del = data.get("mes_to_del")
        mes = await bot.send_message(
            chat_id=message.chat.id, text="пришлите корректную ссылку"
        )
        mes_to_del += [mes.message_id, message.message_id]
        await state.update_data(mes_to_del=mes_to_del)


async def show_links(call: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=td.SHOW_LINKS,
        reply_markup=await ik.get_links_list(),
    )


async def edit_links(call: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Здесь вы можете удалять старые списки, просто выберите их и подтвердите удаление.",
        reply_markup=await ik.get_links_to_del(),
    )


async def confirm_delete(call: types.CallbackQuery, state: FSMContext):
    link_id = call.data.replace("del_", "")
    link: LinkGameList = await admin_db.get_link(link_id)
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f"Вы уверены что хотите удалить {hlink('этот', link.link)} список?",
        reply_markup=await ik.confirm_delete(link_id),
    )


async def delete_link(call: types.CallbackQuery, state: FSMContext):
    link_id = call.data.replace("confirm_", "")
    await admin_db.delete_link(link_id)
    await call.answer(text="Список был удален", show_alert=True)
    await a_p(call=call, state=state)
