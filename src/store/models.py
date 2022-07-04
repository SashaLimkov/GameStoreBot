from django.db import models


# Create your models here.
class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")


class TelegramUser(TimeBasedModel):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name="Имя пользователя")
    user_id = models.BigIntegerField(unique=True, verbose_name="ID пользователя")


class UserRequest(TimeBasedModel):
    class Meta:
        verbose_name = "Заявка на покупку"
        verbose_name_plural = "Заявки на покупку"

    user = models.ForeignKey(
        TelegramUser,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    question = models.CharField(max_length=5000, verbose_name="Запрос")
    state = models.CharField(
        max_length=100, verbose_name="Состояние", default="Открытый вопрос"
    )
    channel_mes_id = models.BigIntegerField()
    chat_mes_id = models.BigIntegerField()


class LinkGameList(TimeBasedModel):
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

    def __str__(self):
        return self.name

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Название ссылки")
    link = models.CharField(max_length=2000, unique=True, verbose_name="Ссылка")
    link_type = models.ForeignKey("LinkType", on_delete=models.CASCADE, verbose_name="Тип")


class LinkType(TimeBasedModel):
    class Meta:
        verbose_name = "Тип Ссылки"
        verbose_name_plural = "Типы Ссылок"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, unique=True, verbose_name="Тип ссылки")


class ConsultantGroup(TimeBasedModel):
    class Meta:
        verbose_name = "Группа консультанта"
        verbose_name_plural = "Группа консультантов"

    id = models.AutoField(primary_key=True)
    chanel_id = models.BigIntegerField(
        unique=True, verbose_name="ID Канала консультантов"
    )
    chat_id = models.BigIntegerField(unique=True, verbose_name="ID Чата консультантов")


class TelegramText(TimeBasedModel):
    class Meta:
        verbose_name = "Тексты бота"
        verbose_name_plural = "Текст из бота"

    def __str__(self):
        return self.title

    title = models.CharField(
        max_length=150, verbose_name="Наименование"
    )
    content = models.TextField(blank=True, verbose_name="Контент")
    ordering = ["-created_at", "title"]
