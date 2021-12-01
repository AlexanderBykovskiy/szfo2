from django.db import models

from szfo.common_models import CommonModel


# Модель для формы обратной связи
class FeedbackModel(CommonModel):
    name = models.CharField(
        max_length=255,
        verbose_name='ФИО',
    )
    phone_number = models.CharField(
        max_length=12,
        verbose_name='Номер телефона',
    )
    email = models.CharField(
        max_length=100,
        verbose_name='Email',
        blank=True,
        null=True,
    )
    message = models.TextField(
        verbose_name='Сообщение',
    )
    processed = models.BooleanField(
        default=False,
        verbose_name='Обработано',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Запрос обратной связи'
        verbose_name_plural = 'Запросы обратной связи'
