# Generated by Django 3.2.9 on 2021-12-06 07:30

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newsmodel_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='cover',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, default=None, null=True, upload_to='images/news/', verbose_name='Обложка новости'),
        ),
    ]
