from django.contrib import admin

from ..models import LinkGameList


class LinksAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "link_type")
    list_display_links = ("name",)


# Register your models here.
admin.site.register(LinkGameList, LinksAdmin)
