from rest_framework import serializers
from food.models import Food, FoodNutrition, Recipe, StepRecipe, FoodIngredient


class FoodNutritionSerializer(serializers.ModelSerializer):
    karbo = serializers.SerializerMethodField() #nama variablenya disesuaikan sama fieldnya di model

    def get_karbo(self, obj):
        data = obj.karbo #ini di cek nama nya di model misal obj.karbo dari fields karbo
        #disini kamu tinggal panggil function nya
        return

    class Meta:
        model = FoodNutrition
        exclude = []


class FoodSerializer(serializers.ModelSerializer):
    nutrition = serializers.SerializerMethodField()

    def get_nutrition(self, obj):
        data = obj.foodnutrition_set.all()
        return FoodNutritionSerializer(instance=data).data

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
