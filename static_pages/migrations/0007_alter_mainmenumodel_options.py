# Generated by Django 3.2.9 on 2021-11-09 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0006_mainmenumodel_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainmenumodel',
            options={'ordering': ['order'], 'verbose_name': 'Пункт главного меню', 'verbose_name_plural': 'Пункты главного меню'},
        ),
    ]