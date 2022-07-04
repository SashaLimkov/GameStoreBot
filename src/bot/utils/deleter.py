from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToDeleteNotFound

from bot.config.loader import bot


async def delete_mes(user_id, message_id):
    try:
        await bot.delete_message(chat_id=user_id, message_id=message_id)
    except MessageToDeleteNotFound:
        print("нет сообщения для удаления")


async def delete_user_message(message: types.Message):
    await delete_mes(user_id=message.chat.id, message_id=message.message_id)


async def delete_bot_messages(user_id: int, state: FSMContext):
    data = await state.get_data()
    mes_to_del = data.get("mes_to_del")
    for mes_id in mes_to_del:
        await delete_mes(user_id=user_id, message_id=mes_id)


def strip_tags(text: str):
    r = text
    if "html" in r:
        r = text.replace("<html>", "")
        r = r.replace("</html>", "")
    if "body" in r:
        r = r.replace("<body>", "")
        r = r.replace("</body>", "")
    if "head" in r:
        r = r.replace("<head>", "")
        r = r.replace("</head>", "")
    if "p" in r:
        r = r.replace("<p>", "")
        r = r.replace("</p>", "")
    if "title" in r:
        r = r.replace("<title>", "")
        r = r.replace("</title>", "")
    if "br" in r:
        r = r.replace("<br>", "")
        r = r.replace("<br />", "")
    if "&nbsp;" in r:
        r = r.replace("&nbsp;", " ")
    return r
