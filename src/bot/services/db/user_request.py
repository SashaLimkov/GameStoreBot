from asgiref.sync import sync_to_async

from store.models import UserRequest


@sync_to_async
def add_user_request(user, question, channel_mes_id):
    try:
        r = UserRequest(
            user=user,
            question=question,
            channel_mes_id=channel_mes_id,
            chat_mes_id=channel_mes_id,
        )
        r.save()
        return r
    except Exception:
        return False


@sync_to_async
def select_user_request_by_mes_id(mes_id):
    return UserRequest.objects.filter(channel_mes_id=mes_id).get()


@sync_to_async
def select_user_request_by_user(user):
    return UserRequest.objects.filter(user=user, state="Открытый вопрос").first()


@sync_to_async
def update_chat_mes_id(pk, chat_mes_id):
    return UserRequest.objects.filter(pk=pk).update(chat_mes_id=chat_mes_id)


@sync_to_async
def select_user_request_by_chat_mes_id(chat_mes_id):
    return UserRequest.objects.filter(chat_mes_id=chat_mes_id).get()


@sync_to_async
def update_state(user):
    return UserRequest.objects.filter(user=user).update(state="Завершенная продажа")
