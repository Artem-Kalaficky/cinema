# Generated by Django 4.0.4 on 2022-05-17 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_remove_carousel_slide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='is_bg',
        ),
    ]
