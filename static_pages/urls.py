from django.urls import path, re_path
from .views import *
from static_pages.views import index_page_view

app_name = 'static_pages'

urlpatterns = [
    re_path(
        r'^(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*/?$)',
        static_page_view,
        name='static_page'
    ),
    path(
        '',
        index_page_view,
        name='index'
    ),
]
