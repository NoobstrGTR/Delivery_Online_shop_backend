# Generated by Django 4.0.6 on 2023-01-02 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_alter_cart_model_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item_model',
            name='price_per_unit',
        ),
    ]
