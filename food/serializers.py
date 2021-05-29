from rest_framework import serializers
from food.models import Food, FoodNutrition, Recipe, StepRecipe


class FoodNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodNutrition
        exclude = []


class FoodSerializer(serializers.ModelSerializer):
    nutrition = serializers.SerializerMethodField()

    def get_nutrition(self, obj):
        return obj.foodnutrition_set.values('protein','carbo','lemak')

    class Meta:
        model = Food
        fields = ('id', 'name', 'kcal', 'nutrition')


class RecipeSerializers(serializers.ModelSerializer):
    step = serializers.SerializerMethodField()
    ingredients = serializers.SerializerMethodField()

    def get_step(self, obj):
        return obj.step.values('step')

    def get_ingredients(self, obj):
        return obj.ingredients.values('food__name', 'count', 'desc')

    class Meta:
        model = Recipe
        exclude = []
