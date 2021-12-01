from django.db import models

from szfo.common_models import SEOModel
from ckeditor_uploader.fields import RichTextUploadingField


# Модель статичных страниц
class StaticPageModel(SEOModel):
    id = models.CharField(
        max_length=25,
        unique=True,
        primary_key=True,
        verbose_name='ID страницы',
    )
    header = models.CharField(
        max_length=255,
        verbose_name='Заголовок страницы',
    )
    content = RichTextUploadingField(
        config_name='default',
        verbose_name='Содержимое',
    )

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return '/' + self.slug + '/'

    class Meta:
        verbose_name = 'Статическая страница'
        verbose_name_plural = 'Статические страницы'


# Модель меню
class MainMenuModel(models.Model):
    label = models.CharField(
        max_length=25,
        verbose_name='Заголовок пункта меню',
    )
    page = models.OneToOneField(
        StaticPageModel,
        on_delete=models.CASCADE,
        verbose_name='Страница',
    )
    order = models.PositiveIntegerField(
        default=10,
        verbose_name='Позиция в списке',
    )

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['order']
        verbose_name = 'Пункт главного меню'
        verbose_name_plural = 'Пункты главного меню'


# Модель блоков данных
class ContentBlockModel(models.Model):
    id = models.CharField(
        max_length=25,
        unique=True,
        primary_key=True,
        verbose_name='ID страницы',
    )
    label = models.CharField(
        max_length=25,
        verbose_name='Заголовок блока',
    )
    content = RichTextUploadingField(
        config_name='default',
        verbose_name='Содержимое блока',
    )

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['label']
        verbose_name = 'Блок данных'
        verbose_name_plural = 'Блоки данных'
