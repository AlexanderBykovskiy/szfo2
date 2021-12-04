from django.urls import path, re_path
from .views import *

app_name = 'news'

urlpatterns = [
    path(
        '',
        NewsList.as_view(),
        name='news_list'
    ),
]
