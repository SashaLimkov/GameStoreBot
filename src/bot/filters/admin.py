from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from bot.config.config import ADMINS


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        user_id = message.chat.id
        return True if user_id in ADMINS else False


