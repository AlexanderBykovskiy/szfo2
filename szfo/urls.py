from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path, include
from szfo.common_views import pageNotFound


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

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
