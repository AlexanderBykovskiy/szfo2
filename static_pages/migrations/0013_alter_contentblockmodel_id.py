# Generated by Django 3.2.9 on 2021-12-23 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0012_alter_contentblockmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentblockmodel',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='ID блока'),
        ),
    ]