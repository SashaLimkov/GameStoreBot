from aiogram.utils.markdown import hlink
from bot.services.db import text as t_db


async def START_MESSAGE():
    return await t_db.get_content_by_title("Стартовое сообщение")


async def GAMES_MM():
    return await t_db.get_content_by_title("Как все происходит (игры)")


async def SUBSCRIPTION_MM():
    return await t_db.get_content_by_title("Подписки")


async def SUBSCRIPTIONS_LIST():
    return await t_db.get_content_by_title("Список подписок")


async def GAME_INSTRUCTION_TEXT_ADMIN():
    return await t_db.get_content_by_title("игры инструкция")


async def BUY_GAME():
    return await t_db.get_content_by_title("Ожидание консультанта")


async def POST_FORM() -> str:
    return await t_db.get_content_by_title("Форма заявки на покупку")


async def CONSULTER_INSTRUCTION() -> str:
    return await t_db.get_content_by_title("Инструкция для консультанта")


async def GAME_INSTRUCTION_TEXT() -> str:
    return await t_db.get_content_by_title("Инструкция по активации ключей")


async def SUCCESS() -> str:
    return await t_db.get_content_by_title("оплата прошла")


async def PHONE() -> str:
    return await t_db.get_content_by_title("какой телефон")


async def ANROID_T() -> str:
    return await t_db.get_content_by_title("андроид турция")


async def APPLE_T() -> str:
    return await t_db.get_content_by_title("айфон турция")


async def APPLE_A() -> str:
    return await t_db.get_content_by_title("айфон аргентина")


async def ANDROID_A() -> str:
    return await t_db.get_content_by_title("андроид аргентина")


async def SUBS_ANDROID() -> str:
    return await t_db.get_content_by_title("Подписки android")


async def SUBS_APPLE() -> str:
    return await t_db.get_content_by_title("Подписки apple")


async def WRITE() -> str:
    return await t_db.get_content_by_title("Активируй, пиши")


async def SUBSCRIPTiON_INSTRUCTION() -> str:
    return await t_db.get_content_by_title("подписки инструкция")


async def SUBSCRIPTiON_INSTRUCTION_USER() -> str:
    return await t_db.get_content_by_title("Инструкция по активации подписок")


ADMIN_PANEL = (
    f"Чтобы добавить новый список, нужно создать его {hlink('ЗДЕСЬ', 'https://telegra.ph/')}\n"
    f"{hlink('ГАЙД', 'https://kj.media/trends/guide-telegraph/')} по телеграфу.\n"
    f"После создания списка, нажми на кнопку publish и скопируй ссылку.\n"
    f"Данную ссылку необходимо прислать на этапе добавления нового списка.\n"
    f"Чтобы удалить старый нужно нажать на соответсвующую кнопу, нажать на 🗑, и подтвердить удаление"
)
ADD_LINK_NAME = "Пожалуйста пришлите название для списка"
ADD_LINK = (
    f"Пожалуйста пришлите ссылку на список в {hlink('телеграфе', 'https://telegra.ph/')}\n"
    f"{hlink('ГАЙД', 'https://kj.media/trends/guide-telegraph/')} по телеграфу.\n"
)
SHOW_LINKS = "Доступные списки игр"
GAME_INSTRUCTION = "Инструкция по активации ключей"
SUBS_INSTRUCTION = "Инструкция по активации ключей"

BACK_TO_MM = "◀ Назад"
BACK_TO_MM_CD = "back"
BACK_TO_A_MM_CD = "a_back"
