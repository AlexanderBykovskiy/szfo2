from django.contrib import admin
from .models import *


@admin.register(NewsModel)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('header', 'author', 'publication_date', 'published',)
    ordering = ['-published']
    list_display_links = ('header',)
    search_fields = ('header', 'author', 'content')
    list_filter = ('author', 'publication_date', 'published')

    fieldsets = (
        ('Основные данные', {'fields': ('header', 'content', 'author', 'publication_date', 'published',)}),
        ('SEO', {'fields': ('slug', 'page_description',)}),
    )
    prepopulated_fields = {'slug': ('header',)}
