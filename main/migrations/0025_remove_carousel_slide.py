# Generated by Django 4.0.4 on 2022-05-17 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_carousel_speed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='slide',
        ),
    ]
