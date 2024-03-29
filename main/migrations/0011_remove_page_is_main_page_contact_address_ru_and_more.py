# Generated by Django 4.0.4 on 2022-05-13 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_newsorprom_description_ru_newsorprom_description_uk_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='is_main_page',
        ),
        migrations.AddField(
            model_name='contact',
            name='address_ru',
            field=models.TextField(null=True, verbose_name='Адресс'),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_uk',
            field=models.TextField(null=True, verbose_name='Адресс'),
        ),
        migrations.AddField(
            model_name='contact',
            name='name_ru',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.cinema', verbose_name='Название кинотеатра'),
        ),
        migrations.AddField(
            model_name='contact',
            name='name_uk',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.cinema', verbose_name='Название кинотеатра'),
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='page',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='page',
            name='description_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='page',
            name='is_base',
            field=models.BooleanField(default=True, verbose_name='Основная страница'),
        ),
        migrations.AddField(
            model_name='page',
            name='name_ru',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='page',
            name='name_uk',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='page',
            name='seo_text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='SEO текст'),
        ),
        migrations.AddField(
            model_name='page',
            name='seo_text_uk',
            field=models.TextField(blank=True, null=True, verbose_name='SEO текст'),
        ),
        migrations.AlterField(
            model_name='page',
            name='date_created',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата создания'),
        ),
    ]
