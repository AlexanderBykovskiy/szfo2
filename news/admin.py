from django.contrib import admin
from .models import *


@admin.register(NewsModel)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('header', 'author', 'publication_date', 'published',)
    ordering = ['-published']
    list_display_links = ('header',)
