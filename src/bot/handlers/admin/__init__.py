from aiogram import Dispatcher
from aiogram.dispatcher import filters

from bot.filters.admin import AdminFilter
from bot.handlers.admin import commands


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.register_message_handler(commands.set_commands, filters.Command("sc"), is_admin=True, state="*")
    dp.register_message_handler(commands.delete_commands, filters.Command("dc"), is_admin=True, state="*")
    dp.register_message_handler(commands.admin_panel, filters.Command("admin"), is_admin=True, state="*")
