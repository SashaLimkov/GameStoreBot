from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


from store.models import TelegramText


class TextAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = TelegramText
        fields = "__all__"


class TelegramTextAdmin(admin.ModelAdmin):
    form = TextAdminForm
    list_display = ["title", "created_at", "updated_at"]
    list_display_links = ["title"]
    search_fields = ["title", "content"]


admin.site.register(TelegramText, TelegramTextAdmin)
