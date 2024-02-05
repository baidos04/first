# Generated by Django 5.0.1 on 2024-01-31 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted')], default='Active', max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enum_type', models.CharField(choices=[('telegram', 'Telegram'), ('phone', 'Phone'), ('instagram', 'instagram')], max_length=50)),
                ('string_value', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='shop.user')),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price_agreeable', models.BooleanField(default=False)),
                ('price', models.FloatField(max_length=155)),
                ('currency', models.CharField(choices=[('som', 'SOM'), ('usd', 'USD'), ('rub', 'RUB')], default='som', max_length=3)),
                ('vip_type', models.CharField(choices=[('normal', 'Normal'), ('vip', 'VIP')], default='normal', max_length=10)),
                ('state', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('moderation', 'Moderation')], default='active', max_length=10)),
                ('images', models.BinaryField(null=True)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('is_liked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='shop.category')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='shop.user')),
            ],
        ),
    ]