from django.contrib import admin
from .models import *


@admin.register(StaticPageModel)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'changed_date', 'created_date',)
    ordering = ['header']
    search_fields = ['header']
    list_display_links = ('header',)

    fieldsets = (
        ('Основные данные', {'fields': ('id', 'header', 'content',)}),
        ('SEO', {'fields': ('slug', 'page_description',)}),
    )
    prepopulated_fields = {'slug': ('id',)}


@admin.register(MainMenuModel)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('label', 'page', 'order',)
    ordering = ['order', 'label']
    list_display_links = ('label',)
    list_editable = ('order',)


@admin.register(ContentBlockModel)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'label',)
    ordering = ['label']
    list_display_links = ('label',)
