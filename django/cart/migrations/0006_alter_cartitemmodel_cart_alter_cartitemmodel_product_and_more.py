# Generated by Django 4.0.6 on 2022-12-04 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0015_alter_productmodel_is_fave'),
        ('cart', '0005_alter_cartitemmodel_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitemmodel',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartmodel', verbose_name='سبدخرید'),
        ),
        migrations.AlterField(
            model_name='cartitemmodel',
            name='product',
            field=models.ManyToManyField(to='product.productmodel', verbose_name='محصولات'),
        ),
        migrations.AlterField(
            model_name='cartitemmodel',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='تعداد محصول'),
        ),
        migrations.AlterField(
            model_name='cartitemmodel',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, verbose_name='قیمت هر تعداد محصول'),
        ),
        migrations.AlterField(
            model_name='cartmodel',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='ایا پرداخت شده ؟'),
        ),
        migrations.AlterField(
            model_name='cartmodel',
            name='total_price',
            field=models.IntegerField(default=0, verbose_name='قیمت کل'),
        ),
        migrations.AlterField(
            model_name='cartmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
