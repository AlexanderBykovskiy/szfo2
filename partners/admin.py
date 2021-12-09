from django.contrib import admin
from .models import *


@admin.register(PartnersModel)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('header', 'link', 'published',)
    ordering = ['header']
    list_display_links = ('header',)
    search_fields = ('header',)
    list_filter = ('published',)

    fieldsets = (
        ('Основные данные', {'fields': ('header', 'logo', 'link_url', 'published',)}),
        ('SEO', {'fields': ('slug', 'page_description',)}),
    )
    prepopulated_fields = {'slug': ('header',)}
