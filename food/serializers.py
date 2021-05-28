from rest_framework import serializers
from food.models import Food, FoodNutrition, Recipe, StepRecipe


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        exclude = []


class FoodNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrition
        exclude = []


class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = []
