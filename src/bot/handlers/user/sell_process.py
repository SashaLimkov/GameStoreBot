from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.data import text_data as td
from bot.config.loader import bot, user_data
from bot.services.db import user_request as u_r
from bot.states import UserState
from bot.utils import deleter
from store.models import TelegramUser, UserRequest
from bot.services.db import user as user_db
from bot.services.db import consult as consult_db
from bot.keyboards import inline as ik


async def wait_for_answer(message: types.Message, state: FSMContext):
    user: TelegramUser = await user_db.select_user(user_id=message.chat.id)
    if await u_r.select_user_request_by_user(user):
        await add_user_text_message(message)
        return
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
        f'<a href="tg://user?id={user.user_id}">{user.name}</a>',
        message.text
    )
    group = await consult_db.get_consult_group()
    chanel_id = group.chanel_id
    mes = await bot.send_message(
        chat_id=chanel_id,
        text=text + "\n<b>НОВАЯ ЗАЯВКА</b>"
    )
    await u_r.add_user_request(user=user, question=text, channel_mes_id=mes.message_id)


async def add_user_text_message(message: types.Message):
    user, u_req, group, chat_id = await get_message_data(message)
    await bot.edit_message_reply_markup(
        chat_id=chat_id,
        message_id=user_data[user.user_id]["last"],
        reply_markup=None
    )
    mes = await bot.send_message(
        chat_id=chat_id,
        reply_to_message_id=u_req.chat_mes_id,
        text=f"{user.name}: {message.text}",
        reply_markup=await ik.consult_quick_menu(user.user_id)
    )
    text = u_req.question + "\n<b>ЕСТЬ НОВЫЕ СООБЩЕНИЯ</b>"

    try:
        await bot.edit_message_text(
            chat_id=group.chanel_id,
            message_id=u_req.channel_mes_id,
            text=text
        )
    except:
        pass
    user_data[user.user_id]["last"] = mes.message_id


async def add_user_photo_message(message: types.Message):
    user, u_req, group, chat_id = await get_message_data(message)
    await bot.edit_message_reply_markup(
        chat_id=chat_id,
        message_id=user_data[user.user_id]["last"],
        reply_markup=None
    )
    mes = await bot.send_photo(
        chat_id=chat_id,
        photo=message.photo[-1].file_id,
        reply_to_message_id=u_req.chat_mes_id,
        caption=f"{user.name}: {message.caption if message.caption else 'Фото от пользователя'}",
        reply_markup=await ik.consult_quick_menu(user.user_id)

    )
    text = u_req.question + "\n<b>ЕСТЬ НОВЫЕ СООБЩЕНИЯ</b>"

    try:
        await bot.edit_message_text(
            chat_id=group.chanel_id,
            message_id=u_req.channel_mes_id,
            text=text
        )
    except:
        pass
    user_data[user.user_id]["last"] = mes.message_id


async def get_message_data(message: types.Message):
    user: TelegramUser = await user_db.select_user(user_id=message.chat.id)
    u_req: UserRequest = await u_r.select_user_request_by_user(user=user)
    print(u_req)
    if not u_req:
        print("Удаление")
        await bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id
        )
    group = await consult_db.get_consult_group()
    chat_id = group.chat_id
    print(user_data[user.user_id])
    return user, u_req, group, chat_id
