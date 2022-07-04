from aiogram import Dispatcher
from aiogram.dispatcher import filters

from bot.handlers.admin.text import send_text


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(
        send_text.game_inst, filters.Text(startswith="send_text_"), state="*"
    )
    dp.register_callback_query_handler(
        send_text.payment, filters.Text(startswith="money_success_"), state="*"
    )
    dp.register_callback_query_handler(
        send_text.user_phone, filters.Text(startswith="user_phone_"), state="*"
    )
    dp.register_callback_query_handler(
        send_text.android_t, filters.Text(startswith="and_t_"), state="*"
    )
    dp.register_callback_query_handler(
        send_text.android_a, filters.Text(startswith="and_a_"), state="*"
    )
    dp.register_callback_query_handler(
        send_text.apple_t, filters.Text(startswith="app_t_"), state="*"
    )
    dp.register_callback_query_handler(
        send_text.apple_a, filters.Text(startswith="app_a_"), state="*"
    )
    dp.register_callback_query_handler(
        send_text.subs, filters.Text(startswith="sub_text_"), state="*"
    )
    dp.register_callback_query_handler(
        send_text.subs_app, filters.Text(startswith="subs_app_"), state="*"
    )
    dp.register_callback_query_handler(
        send_text.subs_and, filters.Text(startswith="subs_and_"), state="*"
    )
    dp.register_callback_query_handler(
        send_text.write, filters.Text(startswith="act_"), state="*"
    )
