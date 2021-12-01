from django.contrib import admin
from .models import *


@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'created_date',)
    ordering = ['-created_date']
    list_display_links = ('name',)
