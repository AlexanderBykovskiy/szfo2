from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from easy_thumbnails.fields import ThumbnailerImageField
from szfo.common_models import SEOModel


# Модель партнеров
class PartnersModel(SEOModel):
    header = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    logo = ThumbnailerImageField(
        upload_to='images/partners/',
        verbose_name='Логотип',
    )
    link_url = models.URLField(
        max_length=512,
        verbose_name='Ссылка (URL)',
    )
    published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
    )

    def __str__(self):
        return self.header

    #def get_absolute_url(self):
    #    return reverse('news:news_item', kwargs={'slug': self.slug})

    @admin.display(description='Ссылка')
    def link(self):
        return format_html('<a href="{}" target="_blank">Перейти на сайт партнера</a>', self.link_url)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ['header']
