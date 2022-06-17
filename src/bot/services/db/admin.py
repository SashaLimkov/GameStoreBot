from asgiref.sync import sync_to_async
from store.models import LinkGameList


@sync_to_async
def add_link(name, link):
    try:
        return LinkGameList(
            name=name, link=link
        ).save()
    except Exception as e:
        print(e)


@sync_to_async
def get_all_links():
    return LinkGameList.objects.all()
