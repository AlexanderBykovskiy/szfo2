from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path(
        r'admin/?',
        admin.site.urls
    ),
    re_path(
        '',
        include('static_pages.urls', namespace='static_pages')
    ),
]
