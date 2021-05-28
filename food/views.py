from rest_framework import viewsets, mixins, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
from food.serializers import FoodSerializer
from food.models import Food


class FoodViewsSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated,]