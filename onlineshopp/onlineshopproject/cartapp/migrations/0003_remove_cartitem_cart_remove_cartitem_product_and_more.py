# Generated by Django 4.1.2 on 2022-11-26 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_alter_cartitem_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
