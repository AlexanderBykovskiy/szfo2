from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from easy_thumbnails.fields import ThumbnailerImageField

from szfo.common_models import SEOModel
from ckeditor_uploader.fields import RichTextUploadingField


# Модель статей
class ArticlesModel(SEOModel):
    header = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
    )
    cover = ThumbnailerImageField(
        upload_to='images/articles/',
        verbose_name='Обложка статьи',
    )
    short_content = models.TextField(
        verbose_name='Тизер',
    )
    content = RichTextUploadingField(
        config_name='default',
        verbose_name='Содержимое',
    )
    pdf_file = models.FileField(
        upload_to='files/articles/%Y/%m',
        verbose_name='Файл pdf',
        blank=True,
        null=True,
        default=None,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    author = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Автор',
    )
    publication_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата публикации',
    )
    published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
    )

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('article_item', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-publication_date']


# Модель публикаций
class PublicationsModel(SEOModel):
    header = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
    )
    cover = ThumbnailerImageField(
        upload_to='images/publications/',
        verbose_name='Обложка публикации',
    )
    source = models.CharField(
        max_length=255,
        verbose_name='Наименование источника',
    )
    source_url = models.URLField(
        max_length=512,
        verbose_name='URL источника',
    )
    publication_date = models.DateField(
        verbose_name='Дата публикации',
    )
    published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
    )

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('publication_item', kwargs={'slug': self.slug})

    @admin.display(description='Ссылка на источник')
    def source_link(self):
        return format_html('<a href="{}" target="_blank">Перейти к источнику</a>', self.source_url)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-publication_date']
