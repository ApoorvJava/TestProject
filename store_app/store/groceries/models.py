from django.db import models

class Fruits(models.Model):
    quantity_choices=(
        (1, 1),
        (5, 5),
        (10, 10)
    )
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(choices = quantity_choices)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Vegetables(models.Model):
    quantity_choices=(
        (1, 1),
        (5, 5),
        (10, 10)
    )
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(choices = quantity_choices)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class BeautyProducts(models.Model):
    quantity_choices=(
        (1, 1),
        (2, 2),
        (3, 3)
    )
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    quantity = models.IntegerField(choices=quantity_choices)
    price = models.IntegerField()

    def __str__(self):
        return self.name
