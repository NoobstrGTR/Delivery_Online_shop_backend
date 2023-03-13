# Generated by Django 4.0.6 on 2022-11-24 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره موبایل')),
                ('sms', models.CharField(max_length=6, verbose_name='SMS')),
            ],
            options={
                'verbose_name': 'اس ام اس',
                'verbose_name_plural': 'اس ام اس',
            },
        ),
        migrations.CreateModel(
            name='StoreCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='دسته فروشگاهی')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'دسته فروشگاهی',
                'verbose_name_plural': 'دسته فروشگاهی',
            },
        ),
        migrations.CreateModel(
            name='StoreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=30, unique=True, verbose_name='نام فروشگاه')),
                ('store_phone_number', models.CharField(blank=True, max_length=8, null=True, verbose_name='تلفن فروشگاه')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=store.models.Profile_image_path, verbose_name='لوگو')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.storecategorymodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'فروشگاه ها ',
                'verbose_name_plural': 'فروشگاه',
            },
        ),
    ]
