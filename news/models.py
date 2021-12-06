from django.db import models
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField

from szfo.common_models import SEOModel
from ckeditor_uploader.fields import RichTextUploadingField


# Модель статичных страниц
class NewsModel(SEOModel):
    header = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
    )
    cover = ThumbnailerImageField(
        upload_to='images/news/',
        verbose_name='Обложка новости',
    )
    content = RichTextUploadingField(
        config_name='default',
        verbose_name='Содержимое',
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
        return reverse('news:news_item', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-publication_date']
