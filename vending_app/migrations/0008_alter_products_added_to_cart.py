# Generated by Django 4.2.1 on 2023-06-09 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending_app', '0007_alter_products_added_to_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='added_to_cart',
            field=models.BooleanField(default='False', verbose_name='added_to_cart'),
        ),
    ]
