from asgiref.sync import sync_to_async

from store.models import ConsultantGroup


@sync_to_async
def add_consult_group(chat_id, chanel_id):
    try:
        return ConsultantGroup(chat_id=chat_id, chanel_id=chanel_id).save()
    except Exception as e:
        print(e)
