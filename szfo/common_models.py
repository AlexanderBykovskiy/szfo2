from django.db import models


# Абстрактная модель с полями дат создания и последнего изменения экземпляра модели
class CommonModel(models.Model):

    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    changed_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения',
    )

    class Meta:
        abstract = True


# Абстрактная модель полей SEO для добавления в модели материалов и статичных страниц
class SEOModel(CommonModel):

    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='URL',
    )
    page_description = models.CharField(
        max_length=1024,
        blank=True,
        null=True,
        verbose_name='Описание для поисковых систем',
    )

    class Meta:
        abstract = True
