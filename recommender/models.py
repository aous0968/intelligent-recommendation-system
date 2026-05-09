from django.db import models

class User(models.Model):
    user_id = models.IntegerField(unique=True)
    age = models.IntegerField()
    country = models.CharField(max_length=100)

class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    category = models.CharField(max_length=100)
    price = models.FloatField()

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()

class Behavior(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    viewed = models.BooleanField(default=False)
    clicked = models.BooleanField(default=False)
    purchased = models.BooleanField(default=False)