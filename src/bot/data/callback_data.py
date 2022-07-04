from aiogram.utils.callback_data import CallbackData

MAIN_MENU = CallbackData("MM", "user_choice")
SUBS_MENU = CallbackData("SM", "user_choice", "s_list")
GAME_INSTRUCTION = CallbackData("GM", "user_choice", "instruction")
SUBS_INSTRUCTION = CallbackData("SM", "user_choice", "instruction")
