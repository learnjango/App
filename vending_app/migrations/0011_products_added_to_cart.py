# Generated by Django 4.2.1 on 2023-06-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vending_app', '0010_remove_products_added_to_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='added_to_cart',
            field=models.CharField(default='False', max_length=10, verbose_name='added_to_cart'),
        ),
    ]