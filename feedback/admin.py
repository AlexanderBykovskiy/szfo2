from django.contrib import admin
from .models import *


@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email', 'created_date', 'processed',)
    search_fields = ['name', 'phone_number', 'email', 'message']
    ordering = ['-created_date']
    list_display_links = ('name',)
    list_filter = ('processed', 'created_date')
