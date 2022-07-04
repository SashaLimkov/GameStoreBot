import json

from store.models import TelegramText, LinkType


def get_text():
    text_obj_lst = TelegramText.objects.all()
    res = {}
    titles = []
    contents = []
    for text in text_obj_lst:
        titles.append(text.title)
        contents.append(text.content)
    res.update({
        "title": titles,
        "content": contents,
    })
    r = json.dumps(res)
    with open("res.json", "w", encoding="utf-8") as file:
        file.write(r)


def init_text():
    with open("res.json") as json_file:
        data = json.load(json_file)
        titles = data["title"]
        contents = data["content"]
        for i in range(len(titles)):
            TelegramText(title=titles[i], content=contents[i]).save()


def init_link_types():
    game = LinkType(name="Игры")
    subs = LinkType(name="Подписки")
    game.save()
    subs.save()


def init_data():
    init_link_types()
    init_text()
