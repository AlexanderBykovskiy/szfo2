from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, path, include
from szfo.common_views import pageNotFound
from news.views import NewsList, NewsItem
from publications.views import ArticlesList, ArticlesItem, PublicationsList #PublicationsItem
from partners.views import PartnersList, PartnersItem


urlpatterns = [
    re_path(
        r'^manage/?',
        admin.site.urls
    ),
    re_path(
        r'^news/?$',
        NewsList.as_view(),
        name='news_list'
    ),
    re_path(
        r'^news/(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)/?$',
        NewsItem.as_view(),
        name='news_item'
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
    re_path(
        r'^publications/?$',
        PublicationsList.as_view(),
        name='publications_list'
    ),
    # re_path(
    #    r'^publications/(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)/?$',
    #    PublicationsItem.as_view(),
    #    name='publication_item'
    # ),
    re_path(
        r'^partners/?$',
        PartnersList.as_view(),
        name='partners_list'
    ),
    re_path(
        r'^partners/(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)/?$',
        PartnersItem.as_view(),
        name='partner_item'
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
