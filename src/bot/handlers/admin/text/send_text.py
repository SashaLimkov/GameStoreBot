from aiogram import types

from bot.config.loader import bot
from bot.data import text_data as td
from bot.services.db import user_request as u_r
from bot.services.db import user as u_db
from bot.services.db import consult as c_db


async def game_inst(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(chat_id=user_id, text=await td.GAME_INSTRUCTION_TEXT_ADMIN())
    await call.answer(text="Отправьте реквизиты пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Инструкция игры отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def payment(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(chat_id=user_id, text=await td.SUCCESS())
    await call.answer(text="Сообщение доставлено пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Оплата прошла отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def user_phone(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(chat_id=user_id, text=await td.PHONE())
    await call.answer(text="Сообщение доставлено пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Какой телефон? отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def android_t(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(chat_id=user_id, text=await td.ANROID_T())
    await call.answer(text="Сообщение доставлено пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Андроид турция отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def android_a(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(chat_id=user_id, text=await td.ANDROID_A())
    await call.answer(text="Сообщение доставлено пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Андроид аргентина отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def apple_t(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(chat_id=user_id, text=await td.APPLE_T())
    await call.answer(text="Сообщение доставлено пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Айфон турция отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def apple_a(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(chat_id=user_id, text=await td.APPLE_A())
    await call.answer(text="Сообщение доставлено пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Айфон аргентина отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def subs(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(chat_id=user_id, text=await td.SUBSCRIPTiON_INSTRUCTION())
    await call.answer(text="Сообщение доставлено пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Подписки инструкция, отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def write(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(
        chat_id=user_id,
        text=await td.WRITE(),
    )
    await call.answer(text="Сообщение доставлено пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Активируй пиши, отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def subs_and(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(chat_id=user_id, text=await td.SUBS_ANDROID())
    await call.answer(text="Сообщение доставлено пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Подписки android инструкция, отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def subs_app(call: types.CallbackQuery):
    user_id = call.data.split("_")[-1]
    await bot.send_message(chat_id=user_id, text=await td.SUBS_APPLE())
    await call.answer(text="Сообщение доставлено пользователю", show_alert=True)
    user = await u_db.select_user(user_id)
    r = await u_r.select_user_request_by_user(user)
    chat = await c_db.get_consult_group()
    await bot.send_message(
        chat_id=chat.chat_id,
        text="Подписки apple инструкция, отправлено пользователю",
        reply_to_message_id=r.chat_mes_id,
    )
    await update_msg(user)


async def update_msg(user):
    u_req = await u_r.select_user_request_by_user(user)
    text = u_req.question
    group = await c_db.get_consult_group()
    chat_id = group.chanel_id
    try:
        await bot.edit_message_text(
            chat_id=chat_id, message_id=u_req.channel_mes_id, text=text
        )
    except:
        pass
