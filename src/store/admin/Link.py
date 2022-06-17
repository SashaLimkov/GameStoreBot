from django.contrib import admin

from ..models import LinkGameList


class LinksAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "link"
    )


# Register your models here.
admin.site.register(LinkGameList, LinksAdmin)
