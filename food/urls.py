from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('bahan', views.FoodViewsSet)
router.register('recipe', views.RecipeViewSet)

urlpatterns = [
    path('nutrition-detail/', views.ListNutritionView.as_view())
]
urlpatterns += router.urls
