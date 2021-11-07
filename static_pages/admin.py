from django.contrib import admin
from .models import *


@admin.register(StaticPageModel)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'changed_date', 'created_date')
    ordering = ['header']
    search_fields = ['header']
    list_display_links = ('header',)

    fieldsets = (
        ('Основные данные', {'fields': ('id', 'header', 'content',)}),
        ('SEO', {'fields': ('slug', 'page_description')}),
    )
