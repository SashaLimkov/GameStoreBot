from aiogram import types

from bot.config.loader import bot, user_data
from bot.services.db import user_request as u_r
from store.models import UserRequest, TelegramUser
from bot.data import text_data as td
from bot.services.db import user as user_db


async def add_admin_menu(message: types.Message):
    r: UserRequest = await u_r.select_user_request_by_mes_id(message.forward_from_message_id)
    if r:
        await u_r.update_chat_mes_id(r.pk, message.message_id)
        mes = await bot.send_message(
            chat_id=message.chat.id,
            reply_to_message_id=message.message_id,
            text=await td.CONSULTER_INSTRUCTION()
        )
        user_data[r.user.user_id].update({"last"})


async def add_admin_text_message(message: types.Message):
    user = await get_message_data(message)
    await bot.send_message(
        chat_id=user.user_id,
        text=f"{message.text}",
    )


async def add_admin_photo_message(message: types.Message):
    user = await get_message_data(message)
    await bot.send_photo(
        chat_id=user.user_id,
        photo=message.photo[-1].file_id,
        caption=f"{message.caption}",
    )


async def get_message_data(message: types.Message):
    u_req: UserRequest = await u_r.select_user_request_by_chat_mes_id(message.reply_to_message.message_id)
    user: TelegramUser = u_req.user
    return user
