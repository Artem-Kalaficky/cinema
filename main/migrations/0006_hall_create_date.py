# Generated by Django 4.0.4 on 2022-05-10 15:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_film_description_ru_film_description_uk_film_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='create_date',
            field=models.DateField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]
