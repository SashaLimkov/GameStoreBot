from django.contrib import admin

from ..models import ConsultantGroup


class ConsultAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "chat_id",
        "chanel_id",
        "created_at",
        "updated_at",
    )


# Register your models here.
admin.site.register(ConsultantGroup, ConsultAdmin)
