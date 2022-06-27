from store.models import LinkGameList, TelegramUser

# from store.models import TelegramUser
from asgiref.sync import sync_to_async


@sync_to_async
def select_user(user_id) -> TelegramUser:
    user = TelegramUser.objects.filter(user_id=user_id).first()
    return user


@sync_to_async
def add_user(user_id, name):
    try:
        r = TelegramUser(user_id=int(user_id), name=name)
        r.save()
        return r
    except Exception:
        return False


@sync_to_async
def get_all_links():
    return LinkGameList.objects.all()
