# Generated by Django 4.0.4 on 2022-05-30 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_mailing_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='name',
        ),
    ]