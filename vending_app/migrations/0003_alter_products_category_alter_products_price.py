# Generated by Django 4.2.1 on 2023-06-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending_app', '0002_products_category_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(max_length=100, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(max_length=10, verbose_name='Price'),
        ),
    ]
