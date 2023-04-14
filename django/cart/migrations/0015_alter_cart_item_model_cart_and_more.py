# Generated by Django 4.0.6 on 2023-04-14 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_cpu_choices_model_alter_productimage_image'),
        ('cart', '0014_alter_cart_item_model_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item_model',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='cart.cart_model', verbose_name='سبد خرید'),
        ),
        migrations.AlterField(
            model_name='cart_item_model',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmodel', verbose_name='محصول'),
        ),
    ]
