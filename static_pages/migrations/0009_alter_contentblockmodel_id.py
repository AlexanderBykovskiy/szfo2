# Generated by Django 3.2.9 on 2021-11-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0008_contentblockmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentblockmodel',
            name='id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False, unique=True, verbose_name='ID страницы'),
        ),
    ]
