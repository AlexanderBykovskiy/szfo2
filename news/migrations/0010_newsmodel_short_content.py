# Generated by Django 3.2.9 on 2021-12-06 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_newsmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='short_content',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Тизер'),
        ),
    ]
