from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToEditNotFound, MessageCantBeEdited

from bot.config.loader import bot
from bot.states.user import UserState
from bot.utils import deleter
from bot.data import text_data as td
from bot.keyboards import inline as ik


async def game_menu(call: types.CallbackQuery, state: FSMContext):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=td.GAMES_MM,
        # reply_markup=
    )
