# Generated by Django 4.0.4 on 2022-05-13 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_contact_address_alter_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='contact',
        ),
    ]
