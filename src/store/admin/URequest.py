from django.contrib import admin

from ..models import UserRequest


class UReqAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "question",
        "channel_mes_id",
        "chat_mes_id",
        "state"
    )
    list_display_links = ["user",]


# Register your models here.
admin.site.register(UserRequest, UReqAdmin)