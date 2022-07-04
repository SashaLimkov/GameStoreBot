from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config.loader import bot, user_data, storage
from bot.services.db import user_request as u_r
from bot.services.db import consult as consult_db
from bot.states import UserState
from store.models import UserRequest, TelegramUser
from bot.data import text_data as td
from bot.keyboards import inline as ik


async def add_admin_menu(message: types.Message):
    r: UserRequest = await u_r.select_user_request_by_mes_id(
        message.forward_from_message_id
    )
    if r:
        await u_r.update_chat_mes_id(r.pk, message.message_id)
        mes = await bot.send_message(
            chat_id=message.chat.id,
            reply_to_message_id=message.message_id,
            text=await td.CONSULTER_INSTRUCTION(),
            reply_markup=await ik.consult_quick_menu(r.user.user_id),
        )
        user_data.update({r.user.user_id: {"last": mes.message_id}})
        print(user_data)


async def add_admin_text_message(message: types.Message, state: FSMContext):
    user = await get_message_data(message)
    if message.text.lower().strip() == "конец":
        await bot.send_message(
            chat_id=user.user_id,
            text=f'Чтобы продолжить пользоваться ботом напишите /start, если что то пошло не так напишите <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>',
        )
        u_state = FSMContext(storage, user.user_id, user.user_id)
        await u_state.set_state(UserState.static)
        u_req = await u_r.select_user_request_by_user(user)
        text = u_req.question
        group = await consult_db.get_consult_group()
        chat_id = group.chanel_id
        try:
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=u_req.channel_mes_id,
                text=text + "\n<b>ПОКУПКА ЗАВЕРШЕНА</b>",
            )
        except:
            pass
        await u_r.update_state(user)
        return

    await bot.send_message(
        chat_id=user.user_id,
        text=f"{message.text}",
    )
    u_req = await u_r.select_user_request_by_user(user)
    text = u_req.question
    print(text)
    group = await consult_db.get_consult_group()
    chat_id = group.chanel_id
    await bot.edit_message_text(
        chat_id=chat_id, message_id=u_req.channel_mes_id, text=text
    )


async def add_admin_photo_message(message: types.Message):
    user = await get_message_data(message)
    await bot.send_photo(
        chat_id=user.user_id,
        photo=message.photo[-1].file_id,
        caption=f"{message.caption}",
    )
    u_req = await u_r.select_user_request_by_user(user)
    text = u_req.question
    group = await consult_db.get_consult_group()
    chat_id = group.chanel_id

    try:
        await bot.edit_message_text(
            chat_id=chat_id, message_id=u_req.channel_mes_id, text=text
        )
    except:
        pass


async def get_message_data(message: types.Message):
    u_req: UserRequest = await u_r.select_user_request_by_chat_mes_id(
        message.reply_to_message.message_id
    )
    user: TelegramUser = u_req.user
    return user
