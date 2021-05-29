from django.db import models

# Create your models here.
from food.models import Recipe
from users.models import User


class FoodsMother(models.Model):
    TYPE = (
        (0, "Sarapan"),
        (1, "Makan Siang"),
        (2, "Makan Malam")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_foods = models.IntegerField(choices=TYPE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateField()


class WaterNutrition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liters = models.IntegerField()
    date = models.DateField()


class MotherNutritionDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    kcal = models.IntegerField()
    carbo = models.IntegerField()
    protein = models.IntegerField()
    lemak = models.IntegerField()

