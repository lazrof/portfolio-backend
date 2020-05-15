from django.contrib import admin

# Register your models here.
from .models import (Post, Tag, Media, Content)

admin.site.register(Post)
admin.site.register(Tag)

@admin.register(Content)
class Content(admin.ModelAdmin):
	list_display = [
        'title',
        'key',
        'post',
        'language_code',
        'order',
        'updated'
    ]


@admin.register(Media)
class Media(admin.ModelAdmin):
	list_display = [
        'file_name',
        'file_type',
        'url'
    ]