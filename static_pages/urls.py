from django.urls import re_path
from .views import *

app_name = 'static_pages'

urlpatterns = [
    re_path(r'^(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*/?$)', static_page_view, name='static_page'),
]
