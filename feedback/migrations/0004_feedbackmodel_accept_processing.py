# Generated by Django 3.2.9 on 2021-12-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_alter_feedbackmodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackmodel',
            name='accept_processing',
            field=models.BooleanField(default=False, verbose_name='ФЗ-152'),
        ),
    ]