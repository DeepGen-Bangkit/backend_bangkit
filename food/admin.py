from django.contrib import admin
from food.models import FoodNutrition, Food, StepRecipe, Recipe, FoodIngredient


class FoodNutritionAdmin(admin.TabularInline):
    model = FoodNutrition
    extra = 0


class FoodIngredientsAdmin(admin.ModelAdmin):
    list_display = ('food','count', )


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'kcal')
    inlines = [FoodNutritionAdmin, ]


class StepRecipeAdmin(admin.ModelAdmin):
    list_display = ('step',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Food, FoodAdmin)
admin.site.register(StepRecipe, StepRecipeAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(FoodIngredient, FoodIngredientsAdmin)

