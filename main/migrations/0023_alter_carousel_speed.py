# Generated by Django 4.0.4 on 2022-05-16 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_carousel_speed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='speed',
            field=models.IntegerField(choices=[(5000, '5с'), (10000, '10с'), (15000, '15с')], verbose_name='Скорость'),
        ),
    ]
