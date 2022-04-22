# Generated by Django 4.0.4 on 2022-04-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='type',
        ),
        migrations.AddField(
            model_name='film',
            name='type_2d',
            field=models.BooleanField(default=True, verbose_name='2D'),
        ),
        migrations.AddField(
            model_name='film',
            name='type_3d',
            field=models.BooleanField(default=False, verbose_name='3D'),
        ),
        migrations.AddField(
            model_name='film',
            name='type_imax',
            field=models.BooleanField(default=False, verbose_name='IMax'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='speed',
            field=models.CharField(choices=[(None, 'Выберете скорость'), ('1', '5c'), ('2', '10c'), ('3', '15')], default='1', max_length=1, verbose_name='Скорость вращения'),
        ),
    ]
