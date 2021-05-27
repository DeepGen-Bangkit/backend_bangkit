from django.contrib import admin

# Register your models here.
from food.models import FoodNutrition, Food, StepRecipe, Recipe


class FoodNutritionAdmin(admin.TabularInline):
    model = FoodNutrition
    extra = 0


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'kcal')
    inlines = [FoodNutritionAdmin, ]


class StepRecipeAdmin(admin.ModelAdmin):
    list_display = ('step',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'step')


admin.site.register(Food, FoodAdmin)
admin.site.register(StepRecipe, StepRecipeAdmin)
admin.site.register(Recipe, RecipeAdmin)
