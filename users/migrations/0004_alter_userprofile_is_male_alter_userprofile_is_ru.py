# Generated by Django 4.0.4 on 2022-05-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_card_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_male',
            field=models.BooleanField(default=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_ru',
            field=models.BooleanField(default=True, verbose_name='Язык'),
        ),
    ]
