# Generated by Django 4.1.2 on 2022-11-24 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshopapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='desc',
            new_name='description',
        ),
    ]
