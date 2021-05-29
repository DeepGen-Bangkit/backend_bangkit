from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('bahan', views.FoodViewsSet)
router.register('recipe', views.RecipeViewSet)

urlpatterns = []
urlpatterns += router.urls
