# Generated by Django 5.0 on 2024-01-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0004_brands_email_nbateam_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nbateam',
            name='image',
        ),
        migrations.AddField(
            model_name='proleague',
            name='start',
            field=models.DateField(default='TBA'),
            preserve_default=False,
        ),
    ]
