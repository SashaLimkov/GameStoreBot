from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToEditNotFound, MessageCantBeEdited

from bot.config.loader import bot
from bot.states.user import UserState
from bot.utils import deleter
from bot.data import text_data as td
from bot.keyboards import inline as ik


async def cmd_start(message: types.Message, state: FSMContext):
    await deleter.delete_mes(message.chat.id, message.message_id)
    await send_main_menu(message=message, state=state)


async def send_main_menu(message: types.Message, state: FSMContext):
    try:
        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=await td.START_MESSAGE(),
            reply_markup=await ik.get_main_menu(),
            disable_web_page_preview=True,
        )
    except MessageToEditNotFound:
        await new_mm(message=message, state=state)
    except MessageCantBeEdited:
        await new_mm(message=message, state=state)


async def new_mm(message: types.Message, state: FSMContext):
    try:
        await deleter.delete_bot_messages(user_id=message.chat.id, state=state)
    except Exception as e:
        print(e)
    mes = await bot.send_message(
        chat_id=message.chat.id,
        text=await td.START_MESSAGE(),
        reply_markup=await ik.get_main_menu(),
        disable_web_page_preview=True,
    )
    await state.update_data(mes_to_del=[mes.message_id])
    await UserState.static.set()


async def get_mm(call: types.CallbackQuery, state: FSMContext):
    await send_main_menu(message=call.message, state=state)
