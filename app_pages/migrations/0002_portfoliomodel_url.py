# Generated by Django 5.1.5 on 2025-01-21 18:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomodel',
            name='url',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
