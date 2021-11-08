# Generated by Django 3.2.9 on 2021-11-08 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25, verbose_name='Заголовок пункта меню')),
                ('link', models.CharField(max_length=255, verbose_name='ID страницы или URL')),
            ],
            options={
                'verbose_name': 'Пункт главного меню',
                'verbose_name_plural': 'Мункты главного меню',
            },
        ),
    ]
