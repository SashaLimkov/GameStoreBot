from django.db import models


# Create your models here.
class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(auto_now=True)


class TelegramUser(TimeBasedModel):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, verbose_name="UserID")


class LinkGameList(TimeBasedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="LinkName")
    link = models.CharField(max_length=2000, unique=True, verbose_name="Link")
