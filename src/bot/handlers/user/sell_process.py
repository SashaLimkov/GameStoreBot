from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.data import text_data as td
from bot.config.loader import bot
from bot.services.db import user_request as u_r
from bot.states import UserState
from bot.utils import deleter
from store.models import TelegramUser, UserRequest
from bot.services.db import user as user_db
from bot.services.db import consult as consult_db


async def wait_for_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()
    mes_to_del = data.get("mes_to_del")
    await deleter.delete_bot_messages(message.chat.id, state)
    mes = await bot.send_message(
        chat_id=message.chat.id,
        text=await td.BUY_GAME()
    )
    mes_to_del.append(mes.message_id)
    await state.update_data(mes_to_del=mes_to_del)
    await UserState.wait_until_complete.set()
    await create_user_request_post(message=message)


async def create_user_request_post(message: types.Message):
    user: TelegramUser = await user_db.select_user(user_id=message.chat.id)
    text = await td.POST_FORM()
    text = text.format(
        user.name,
        message.text
    )
    group = await consult_db.get_consult_group()
    chanel_id = group.chanel_id
    mes = await bot.send_message(
        chat_id=chanel_id,
        text=text,
    )
    await u_r.add_user_request(user=user, question=text, channel_mes_id=mes.message_id)


async def add_user_text_message(message: types.Message):
    user, u_req, group, chat_id = await get_message_data(message)
    await bot.send_message(
        chat_id=chat_id,
        reply_to_message_id=u_req.chat_mes_id,
        text=f"{user.name}: {message.text}",
    )


async def add_user_photo_message(message: types.Message):
    user, u_req, group, chat_id = await get_message_data(message)
    await bot.send_photo(
        chat_id=chat_id,
        photo=message.photo[-1].file_id,
        reply_to_message_id=u_req.chat_mes_id,
        caption=f"{user.name}: {message.caption}",
    )


async def get_message_data(message: types.Message):
    user: TelegramUser = await user_db.select_user(user_id=message.chat.id)
    u_req: UserRequest = await u_r.select_user_request_by_user(user=user)
    group = await consult_db.get_consult_group()
    chat_id = group.chat_id
    return user, u_req, group, chat_id
