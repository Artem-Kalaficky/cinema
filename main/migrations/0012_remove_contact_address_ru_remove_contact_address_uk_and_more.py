# Generated by Django 4.0.4 on 2022-05-13 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_page_is_main_page_contact_address_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address_ru',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='address_uk',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name_uk',
        ),
    ]
