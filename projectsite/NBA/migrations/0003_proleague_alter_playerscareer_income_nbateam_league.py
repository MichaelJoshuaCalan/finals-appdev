# Generated by Django 5.0 on 2024-01-02 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBA', '0002_rename_years_playerscareer_seasons'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProLeague',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='playerscareer',
            name='Income',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
        migrations.AddField(
            model_name='nbateam',
            name='league',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NBA.proleague'),
        ),
    ]
