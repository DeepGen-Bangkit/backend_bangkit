from rest_framework import serializers
from mainproccess.models import FoodsMother, WaterNutrition, MotherNutritionDetail


class FoodsMotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodsMother
        exclude = ['id']


class WaterNutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterNutrition
        exclude = ['id']


class MotherNutritionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherNutritionDetail
        exclude = ['id']
