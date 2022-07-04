from bot.utils.deleter import strip_tags
from store.models import TelegramText


async def get_content_by_title(title: str):
    r = TelegramText.objects.get(title=title)
    res = strip_tags(r.content).strip()
    return res
