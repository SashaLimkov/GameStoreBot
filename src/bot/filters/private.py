from aiogram.dispatcher.filters import BoundFilter


class PrivateChatFilter(BoundFilter):
    key = "is_private"

    def __init__(self, is_private):
        self.is_private = is_private

    async def check(self, message):
        try:
            chat_type = message.chat.type
        except AttributeError:
            chat_type = message.message.chat.type
        return True if chat_type == "private" else False
