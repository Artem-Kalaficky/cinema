# Generated by Django 4.0.4 on 2022-05-13 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_page_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.contact', verbose_name='Контанкты'),
        ),
    ]
