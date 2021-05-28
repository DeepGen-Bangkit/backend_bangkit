from rest_framework import routers
from django.urls import path, re_path
from . import views

router = routers.SimpleRouter()
router.register('bahan', views.FoodViewsSet)

urlpatterns = []
urlpatterns += router.urls
