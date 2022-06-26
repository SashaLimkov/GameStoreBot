from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageToEditNotFound, MessageCantBeEdited

from bot.config.loader import bot
from bot.handlers.user.commands import send_main_menu
from bot.states.user import UserState
from bot.utils import deleter
from bot.data import text_data as td
from bot.keyboards import inline as ik


async def game_menu(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=await td.GAMES_MM(),
        reply_markup=await ik.get_games_menu(callback_data),
    )


async def get_instruction(
    call: types.CallbackQuery, callback_data: dict, state: FSMContext
):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=await td.GAME_INSTRUCTION_TEXT(),
        reply_markup=await ik.back(callback_data),
    )
