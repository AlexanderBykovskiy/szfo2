from django.db import models
from szfo.common_models import CommonModel


class SEOModel(CommonModel):

    id = models.CharField(
        max_length=25,
        unique=True,
        verbose_name='ID страницы',
    )
    header = models.CharField(
        max_length=255,
        verbose_name='Заголовок страницы',
    )
    #content =


