# Generated by Django 3.2.9 on 2021-12-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedbackmodel_processed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
    ]
