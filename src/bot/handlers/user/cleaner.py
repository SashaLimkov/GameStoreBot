from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config.loader import bot


async def clean_s(message: types.Message, state: FSMContext):
    print(message)
    try:
        await bot.delete_message(
            chat_id=message.chat.id, message_id=message.message_id
        )
        await state.finish()
    except Exception as e:
        print(e)


async def check(message: types.Message, state: FSMContext):
    print(message)