from django_filters import filters
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
import django_filters
# Create your views here.
from food.serializers import FoodSerializer, RecipeSerializers
from food.models import Food, Recipe


class MultiNameFilter(django_filters.Filter):
    def filter(self, qs, value):
        if not value:
            return qs
        if isinstance(value, list):
            return qs.filter(name__in=value)
        elif isinstance(value, str):
            return qs.filter(name__iregex=value)
        else:
            value = value.split(',')
            return qs.filter(name__in=value)


class FoodRecipeFilter(django_filters.Filter):

    def filter(self, qs, value):
        if not value:
            return qs
        if isinstance(value, list):
            return qs.filter(ingredients__food__name__in=value)
        elif isinstance(value, str):
            return qs.filter(ingredients__food__name__iregex=value)
        else:
            value = value.split(',')
            return qs.filter(ingredients__food__name__in=value)


class FoodFilter(django_filters.rest_framework.FilterSet):
    name = MultiNameFilter()

    class Meta:
        model = Food
        fields = ['name']


class FoodRecipeFilter(django_filters.rest_framework.FilterSet):
    ingredients = FoodRecipeFilter()

    class Meta:
        model = Recipe
        fields = ['ingredients']


class FoodViewsSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filterset_class = FoodFilter


class RecipeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
    filterset_class = FoodRecipeFilter
