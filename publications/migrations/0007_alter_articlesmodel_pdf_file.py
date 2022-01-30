# Generated by Django 3.2.9 on 2022-01-30 11:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_alter_articlesmodel_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesmodel',
            name='pdf_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='files/articles/%Y/%m', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Файл pdf'),
        ),
    ]
