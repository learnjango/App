from django.db import models

class Products(models.Model):
    name = models.CharField('Name', max_length=30)
    price = models.IntegerField('Price', max_length=10)
    category = models.CharField('Category', max_length=100)
    img_link = models.CharField('Link', max_length=255, default='unknown')

    def __str__(self):
        return self.name

