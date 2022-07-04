from aiogram import Dispatcher
from aiogram.dispatcher import filters
from aiogram.types import ContentTypes

from bot.config.config import ADMINS
from bot.filters.admin import AdminFilter
from bot.filters.private import PrivateChatFilter
from bot.handlers.admin import commands, links, sell_process, text
from bot.states import UserState


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(PrivateChatFilter)
    text.setup(dp)
    dp.register_message_handler(
        commands.set_consult_group,
        filters.Command("setup_cg"),
        lambda message: message.from_user.id in ADMINS,
        state="*",
    )
    dp.register_message_handler(
        commands.set_commands, filters.Command("sc"), is_admin=True, state="*"
    )
    dp.register_message_handler(
        commands.delete_commands, filters.Command("dc"), is_admin=True, state="*"
    )
    dp.register_message_handler(
        commands.admin_panel, filters.Command("admin"), is_admin=True, state="*"
    )
    dp.register_callback_query_handler(
        links.add_link_name, filters.Text("add"), is_admin=True, state="*"
    )
    dp.register_callback_query_handler(
        links.show_links, filters.Text("show"), is_admin=True, state="*"
    )
    dp.register_callback_query_handler(
        links.edit_links, filters.Text("edit"), is_admin=True, state="*"
    )
    dp.register_callback_query_handler(
        links.confirm_delete, filters.Text(startswith="del_"), is_admin=True, state="*"
    )
    dp.register_callback_query_handler(
        links.delete_link, filters.Text(startswith="confirm_"), is_admin=True, state="*"
    )
    dp.register_callback_query_handler(
        links.a_p, filters.Text("a_back"), is_admin=True, state="*"
    )
    dp.register_message_handler(
        links.add_link, is_admin=True, state=UserState.add_link_name
    )
    dp.register_message_handler(
        links.finish_adding_link, is_admin=True, state=UserState.add_link
    )
    dp.register_message_handler(
        sell_process.add_admin_menu,
        lambda message: "forward_from_message_id" in message,
    )

    dp.register_message_handler(
        sell_process.add_admin_text_message,
        lambda message: "reply_to_message" in message,
        state="*",
    )
    dp.register_message_handler(
        sell_process.add_admin_photo_message,
        lambda message: "reply_to_message" in message,
        content_types=ContentTypes.PHOTO,
        state="*",
    )
