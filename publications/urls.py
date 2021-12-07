from django.urls import path, re_path
from .views import *

app_name = 'publications'

urlpatterns = [
    #re_path(
    #    r'^(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)/?$',
    #    ArticlesItem.as_view(),
    #    name='article_item'
    #),
]
