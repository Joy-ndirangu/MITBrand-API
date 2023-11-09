from django.db import models

# Create your models here.

class Clothes(models.Model):
    item_name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="Description")
    image = models.ImageField(upload_to="clothes", default="clothes/product.png")


    def __str__(self):
        self.item_name
