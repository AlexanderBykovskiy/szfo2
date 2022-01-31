from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField

from szfo.common_models import SEOModel
from ckeditor_uploader.fields import RichTextUploadingField


# Модель новостей
class NewsModel(SEOModel):
    header = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
    )
    cover = ThumbnailerImageField(
        upload_to='images/news/',
        verbose_name='Обложка новости',
    )
    short_content = models.TextField(
        verbose_name='Тизер',
    )
    content = RichTextUploadingField(
        config_name='default',
        verbose_name='Содержимое',
    )
    video_file = models.FileField(
        upload_to='files/video/%Y/%m',
        verbose_name='Файл видео',
        blank=True,
        null=True,
        default=None,
        validators=[FileExtensionValidator(allowed_extensions=['avi', 'wmv', 'mov', 'mkv', '3gp', 'mpeg', 'mpeg-2', 'mpeg-4', 'mp4'])]
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
        return reverse('news_item', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-publication_date']
