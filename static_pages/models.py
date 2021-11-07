from django.db import models
from szfo.common_models import CommonModel
from ckeditor_uploader.fields import RichTextUploadingField


class StaticPageModel(CommonModel):

    id = models.CharField(
        max_length=25,
        unique=True,

    )
    header = models.CharField(
        max_length=255,
        verbose_name='Заголовок страницы',
    )
    content = RichTextUploadingField(
        config_name='default',
        verbose_name='Содержимое',
    )

    class Meta:
        verbose_name = 'Статическая страница'
        verbose_name_plural = 'Статические страницы'

    def __str__(self):
        return self.header
