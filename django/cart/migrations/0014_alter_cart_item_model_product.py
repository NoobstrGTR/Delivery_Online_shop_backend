# Generated by Django 4.0.6 on 2023-01-28 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_cpu_choices_model_alter_productimage_image'),
        ('cart', '0013_remove_cart_item_model_increment_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item_model',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='product.productmodel', verbose_name='محصول'),
        ),
    ]
