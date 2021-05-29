from rest_framework import viewsets, mixins, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
from food.serializers import FoodSerializer, RecipeSerializers
from food.models import Food, Recipe


class FoodViewsSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated,]


class RecipeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
    permission_classes = [IsAuthenticated, ]
