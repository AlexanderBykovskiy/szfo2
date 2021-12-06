from django.urls import path, re_path
from .views import *

app_name = 'news'

urlpatterns = [

    re_path(
        r'^(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)/?$',
        NewsItem.as_view(),
        name='news_item'
    ),
]
