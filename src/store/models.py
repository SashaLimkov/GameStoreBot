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

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, verbose_name="ID пользователя")


class LinkGameList(TimeBasedModel):
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

    def __str__(self):
        return self.name

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Название ссылки")
    link = models.CharField(max_length=2000, unique=True, verbose_name="Ссылка")


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
