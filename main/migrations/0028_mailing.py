# Generated by Django 4.0.4 on 2022-05-30 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_slide_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.FileField(upload_to='archives/', verbose_name='Письмо')),
            ],
            options={
                'verbose_name': 'E-mail',
                'verbose_name_plural': 'E-mails',
            },
        ),
    ]