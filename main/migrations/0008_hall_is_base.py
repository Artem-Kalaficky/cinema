# Generated by Django 4.0.4 on 2022-05-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cinema_condition_ru_cinema_condition_uk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='is_base',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
