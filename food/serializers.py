from rest_framework import serializers
from food.models import Food, FoodNutrition, Recipe, StepRecipe, FoodIngredient


class FoodNutritionSerializer(serializers.ModelSerializer):
    karbo = serializers.SerializerMethodField() #nama variablenya disesuaikan sama fieldnya di model    protein = serializers.SerializerMethodField()
    lemak = serializers.SerializerMethodField()
    air = serializers.SerializerMethodField()
    energi = serializers.SerializerMethodField() #nama variablenya disesuaikan sama fieldnya di model
    serat = serializers.SerializerMethodField()
    abu = serializers.SerializerMethodField()
    kalsium = serializers.SerializerMethodField()
    fosfor = serializers.SerializerMethodField() #nama variablenya disesuaikan sama fieldnya di model
    natrium = serializers.SerializerMethodField()
    besi = serializers.SerializerMethodField()
    kalium = serializers.SerializerMethodField()
    tembaga = serializers.SerializerMethodField()
    seng = serializers.SerializerMethodField()
    retinol = serializers.SerializerMethodField() #nama variablenya disesuaikan sama fieldnya di model
    b_kar = serializers.SerializerMethodField()
    kar_total = serializers.SerializerMethodField()
    thiamin = serializers.SerializerMethodField()
    riboflavin = serializers.SerializerMethodField()
    niasin = serializers.SerializerMethodField()
    vit_c = serializers.SerializerMethodField()

    def get_karbo(self, obj):
        data = obj.karbo #ini di cek nama nya di model misal obj.karbo dari fields karbo
        #disini kamu tinggal panggil function nya
        return

    def get_protein(self, obj):
        data = obj.protein
        return

    def get_lemak(self, obj):
        data = obj.lemak
        return

    def get_air(self, obj):
        data = obj.air
        return

    def get_energi(self, obj):
        data = obj.energi
        return

    def get_serat(self, obj):
        data = obj.serat
        return

    def get_abu(self, obj):
        data = obj.abu
        return

    def get_kalsium(self, obj):
        data = obj.kalsium
        return

    def get_fosfor(self, obj):
        data = obj.fosfor
        return

    def get_natrium(self, obj):
        data = obj.natrium
        return

    def get_besi(self, obj):
        data = obj.besi
        return

    def get_kalium(self, obj):
        data = obj.kalium
        return

    def get_tembaga(self, obj):
        data = obj.tembaga
        return

    def get_seng(self, obj):
        data = obj.seng
        return

    def get_retinol(self, obj):
        data = obj.retinol
        return

    def get_b_kar(self, obj):
        data = obj.b_kar
        return

    def get_kar_total(self, obj):
        data = obj.kar_total
        return

    def get_thiamin(self, obj):
        data = obj.thiamin
        return

    def get_riboflavin(self, obj):
        data = obj.riboflavin
        return

    def get_niasin(self, obj):
        data = obj.niasin
        return

    def get_vit_c(self, obj):
        data = obj.vit_c
        return


    class Meta:
        model = FoodNutrition
        exclude = []


class FoodSerializer(serializers.ModelSerializer):
    nutrition = serializers.SerializerMethodField()

    def get_nutrition(self, obj):
        data = obj.foodnutrition_set.all()
        return FoodNutritionSerializer(instance=data).data

    class Meta:
        model = Food
        fields = ('id', 'name', 'kcal', 'nutrition')


class RecipeSerializers(serializers.ModelSerializer):
    step = serializers.SerializerMethodField()
    ingredients = serializers.SerializerMethodField()

    def get_step(self, obj):
        return obj.step.values('step')

    def get_ingredients(self, obj):
        return obj.ingredients.values('food__name', 'count', 'desc')

    class Meta:
        model = Recipe
        exclude = []
