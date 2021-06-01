from django_filters import filters
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
import django_filters
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from food.serializers import FoodSerializer, RecipeSerializers
from food.models import Food, Recipe, FoodNutrition
from food.utils import count_nutrition


class MultiNameFilter(django_filters.Filter):
    def filter(self, qs, value):
        if not value:
            return qs
        if isinstance(value, list):
            return qs.filter(name__in=value)
        elif isinstance(value, str):
            values = value.split(',')
            lens = len(values)
            if len(values) not in [0, 1] and values[lens-1] != '':
                return qs.filter(name__in=values)
            return qs.filter(name__iregex=value)


class FoodRecipeFilter(django_filters.Filter):

    def filter(self, qs, value):
        if not value:
            return qs
        if isinstance(value, list):
            return qs.filter(ingredients__food__name__in=value)
        elif isinstance(value, str):
            values = value.split(',')
            lens = len(values)
            if len(values) not in [0, 1] and values[lens-1] != '':
                return qs.filter(ingredients__food__name__in=values)
            return qs.filter(ingredients__food__name__iregex=value)


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

    def get_serializer_context(self):
        context = super(FoodViewsSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class RecipeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
    filterset_class = FoodRecipeFilter

    def get_serializer_context(self):
        context = super(RecipeViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class ListNutritionView(APIView):

    def post(self, request, *args):
        data = request.data
        food_nutrition = []
        for d in data:
            try:
                food_name = Food.objects.get(name=d['name'])
            except Food.DoesNotExist:
                ret = {
                    "msg": "Bahan Makanan {} Tidak Ditemukan".format(d)
                }
                food_nutrition.append(ret)
            food = {}
            nutrition = FoodNutrition.objects.filter(food__name=d['name']).values()
            food['name'] = d['name']
            count_nutritions = {}
            for key, values in nutrition[0].items():
                if key not in ['id', 'food_id']:
                    count_nutritions[key] = count_nutrition(values, d['count'], key)
            food['nutrition'] = count_nutritions
            food['kcal'] = round(food_name.kcal * (d['count'] / 100), 2)
            food['count'] = d['count']
            food_nutrition.append(food)
        return Response(food_nutrition, status=status.HTTP_200_OK)
