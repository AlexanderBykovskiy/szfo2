from django.contrib import admin
from .models import *


@admin.register(StaticPageModel)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'content')
    ordering = ['header']
    search_fields = ['header']
    list_display_links = ('header',)
