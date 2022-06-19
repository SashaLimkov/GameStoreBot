from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToEditNotFound, MessageCantBeEdited

from bot.config.loader import bot
from bot.services.db.consult import add_consult_group
from bot.states import UserState
from bot.utils import deleter
from bot.utils.commands_setter import set_default_commands, delete_default_commands
from bot.utils.deleter import delete_user_message
from bot.data import text_data as td
from bot.keyboards import inline as ik


async def admin_panel(message: types.Message, state: FSMContext):
    await delete_user_message(message=message)
    await send_admin_panel(message=message, state=state)


async def send_admin_panel(message: types.Message, state: FSMContext):
    try:
        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=td.ADMIN_PANEL,
            reply_markup=await ik.get_admin_panel(),
            disable_web_page_preview=True
        )
    except MessageToEditNotFound:
        await new_app(message=message, state=state)
    except MessageCantBeEdited:
        await new_app(message=message, state=state)


async def new_app(message: types.Message, state: FSMContext):
    try:
        await deleter.delete_bot_messages(
            user_id=message.chat.id,
            state=state
        )
    except Exception as e:
        print(e)
    mes = await bot.send_message(
        chat_id=message.chat.id,
        text=td.ADMIN_PANEL,
        reply_markup=await ik.get_admin_panel(),
        disable_web_page_preview=True
    )
    await state.update_data(
        mes_to_del=[mes.message_id]
    )
    await UserState.static.set()


async def set_commands(message: types.Message, state: FSMContext):
    await delete_user_message(message=message)
    data = await state.get_data()
    mes_to_del: list = data.get("mes_to_del")
    await set_default_commands()
    mes = await bot.send_message(
        chat_id=message.chat.id,
        text="Команды были установлены"
    )
    mes_to_del.append(mes.message_id)
    await state.update_data(mes_to_del=mes_to_del)


async def delete_commands(message: types.Message, state: FSMContext):
    await delete_user_message(message=message)
    data = await state.get_data()
    mes_to_del: list = data.get("mes_to_del")
    mes = await bot.send_message(
        chat_id=message.chat.id,
        text="Команды были удалены"
    )
    await delete_default_commands()
    mes_to_del.append(mes.message_id)
    await state.update_data(mes_to_del=mes_to_del)


async def set_consult_group(message: types.Message, state: FSMContext):
    chanel_id = message.sender_chat.id
    chat_id = message.chat.id
    await add_consult_group(chat_id=chat_id, chanel_id=chanel_id)
    await bot.send_message(
        chat_id=chanel_id,
        text="Данная группа была установлена как группа админов.\n"
             "Здесь будут появляться заявки от пользователей на приобретение."
    )
