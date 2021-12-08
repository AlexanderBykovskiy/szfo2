from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path, include
from szfo.common_views import pageNotFound
from news.views import NewsList
from publications.views import ArticlesList, ArticlesItem


urlpatterns = [
    re_path(
        r'^admin/?',
        admin.site.urls
    ),
    re_path(
        r'^news/?$',
        NewsList.as_view(),
        name='news_list'
    ),
    re_path(
        r'^news/',
        include('news.urls', namespace='news')
    ),
    re_path(
        r'^articles/?$',
        ArticlesList.as_view(),
        name='articles_list'
    ),
    re_path(
        r'^articles/(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)/?$',
        ArticlesItem.as_view(),
        name='article_item'
    ),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path(
        '',
        include('static_pages.urls', namespace='static_pages')
    ),
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
