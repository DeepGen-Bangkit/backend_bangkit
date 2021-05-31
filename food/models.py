from django.db import models


# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='food/', null=True)
    kcal = models.IntegerField()

    def __str__(self):
        return self.name


class FoodNutrition(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    protein = models.FloatField()
    carbo = models.FloatField()
    lemak = models.FloatField()
    energi = models.FloatField()
    air = models.FloatField()
    serat = models.FloatField()
    abu = models.FloatField()
    kalsium = models.FloatField()
    fosfor = models.FloatField()
    besi = models.FloatField()
    natrium = models.FloatField()
    kalium = models.FloatField()
    tembaga = models.FloatField()
    seng = models.FloatField()
    retinol = models.FloatField()
    b_kar = models.FloatField()
    kar_total = models.FloatField()
    thiamin = models.FloatField()
    riboflavin = models.FloatField()
    niasin = models.FloatField()
    vit_c = models.FloatField()

    def __str__(self):
        return "{} {} ".format(self.food.name, self.food)


class StepRecipe(models.Model):
    step = models.TextField()

    def __str__(self):
        return self.step


class FoodIngredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.food.name, self.count)


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipe/', null=True)
    step = models.ManyToManyField(StepRecipe)
    ingredients = models.ManyToManyField(FoodIngredient)



