from django.db import models


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=200)
    kcal = models.IntegerField()

    def __str__(self):
        return self.name


class FoodNutrition(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    protein = models.FloatField()
    carbo = models.FloatField()
    lemak = models.FloatField()

    def __str__(self):
        return "{} {} ".format(self.food.name, self.food)


class StepRecipe(models.Model):
    step = models.TextField()

    def __str__(self):
        return self.step


class FoodIngredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.FloatField()
    desc = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.food.name, self.count)


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    step = models.ManyToManyField(StepRecipe)
    ingredients = models.ManyToManyField(FoodIngredient)



