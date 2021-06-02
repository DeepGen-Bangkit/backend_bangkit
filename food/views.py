from django_filters import filters
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
import django_filters
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from food.serializers import FoodSerializer, RecipeSerializers
from food.models import Food, Recipe, FoodNutrition
from food.utils import count_nutrition, convert_mg_to_g, count_presentation


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
        kcal_total = 0
        lemak_total = 0
        protein_total = 0
        carbo_total = 0
        total_nutrition = 0
        for d in data:
            try:
                food_name = Food.objects.get(name=d['name'])
            except Food.DoesNotExist:
                ret = {
                    "msg": "Bahan Makanan {} Tidak Ditemukan".format(d['name'])
                }
                food_nutrition.append(ret)
                return Response(food_nutrition, status=status.HTTP_400_BAD_REQUEST)
            food = {}
            nutrition = FoodNutrition.objects.filter(food__name=d['name']).values()
            food['name'] = d['name']
            count_nutritions = {}
            for key, values in nutrition[0].items():
                if key not in ['id', 'food_id']:
                    count_nutritions[key] = count_nutrition(values, d['count'], key)
                    total_nutrition += convert_mg_to_g(key, count_nutritions[key])
            food['nutrition'] = count_nutritions
            food['kcal'] = round(food_name.kcal * (d['count'] / 100), 2)
            food['count'] = d['count']
            kcal_total += food['kcal']
            lemak_total += float(count_nutritions['lemak'].split(' ')[0])
            protein_total += float(count_nutritions['protein'].split(' ')[0])
            carbo_total += float(count_nutritions['carbo'].split(' ')[0])
            food_nutrition.append(food)
        ret = {
            "lemak_total": "{} {}".format(lemak_total, "g"),
            "lemak_presentase": count_presentation(lemak_total, total_nutrition),
            "protein_total": "{} {}".format(protein_total, "g"),
            "protein_presentase": count_presentation(protein_total, total_nutrition),
            "carbo_total": "{} {}".format(carbo_total, "g"),
            "carbo_presentase": count_presentation(carbo_total, total_nutrition),
            "food": food_nutrition
        }
        return Response(ret, status=status.HTTP_200_OK)
