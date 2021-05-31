from rest_framework import serializers
from food.models import Food, FoodNutrition, Recipe, FoodIngredient
from food.utils import count_nutrition


class FoodNutritionSerializer(serializers.ModelSerializer):
    food = serializers.CharField(source='food.name')
    carbo = serializers.SerializerMethodField()
    protein = serializers.SerializerMethodField()
    lemak = serializers.SerializerMethodField()
    air = serializers.SerializerMethodField()
    energi = serializers.SerializerMethodField()
    serat = serializers.SerializerMethodField()
    abu = serializers.SerializerMethodField()
    kalsium = serializers.SerializerMethodField()
    fosfor = serializers.SerializerMethodField()
    natrium = serializers.SerializerMethodField()
    besi = serializers.SerializerMethodField()
    kalium = serializers.SerializerMethodField()
    tembaga = serializers.SerializerMethodField()
    seng = serializers.SerializerMethodField()
    retinol = serializers.SerializerMethodField()
    b_kar = serializers.SerializerMethodField()
    kar_total = serializers.SerializerMethodField()
    thiamin = serializers.SerializerMethodField()
    riboflavin = serializers.SerializerMethodField()
    niasin = serializers.SerializerMethodField()
    vit_c = serializers.SerializerMethodField()

    def get_carbo(self, obj):
        data = obj.carbo
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'carbo')
        return data

    def get_protein(self, obj):
        data = obj.protein
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'protein')
        return data

    def get_lemak(self, obj):
        data = obj.lemak
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'lemak')
        return data

    def get_air(self, obj):
        data = obj.air
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'air')
        return data

    def get_energi(self, obj):
        data = obj.energi
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'energi')
        return data

    def get_serat(self, obj):
        data = obj.serat
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'serat')
        return data

    def get_abu(self, obj):
        data = obj.abu
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'abu')
        return data

    def get_kalsium(self, obj):
        data = obj.kalsium
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'kalsium')
        return data

    def get_fosfor(self, obj):
        data = obj.fosfor
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'fosfor')
        return data

    def get_natrium(self, obj):
        data = obj.natrium
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'natrium')
        return data

    def get_besi(self, obj):
        data = obj.besi
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'besi')
        return data

    def get_kalium(self, obj):
        data = obj.kalium
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'kalium')
        return data

    def get_tembaga(self, obj):
        data = obj.tembaga
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'tembaga')
        return data

    def get_seng(self, obj):
        data = obj.seng
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'seng')
        return data

    def get_retinol(self, obj):
        data = obj.retinol
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'retinol')
        return data

    def get_b_kar(self, obj):
        data = obj.b_kar
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'b_kar')
        return data

    def get_kar_total(self, obj):
        data = obj.kar_total
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'kar_total')
        return data

    def get_thiamin(self, obj):
        data = obj.thiamin
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'thiamin')
        return data

    def get_riboflavin(self, obj):
        data = obj.riboflavin
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'riboflavin')
        return data

    def get_niasin(self, obj):
        data = obj.niasin
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'niasin')
        return data

    def get_vit_c(self, obj):
        data = obj.vit_c
        if self.context['request'].GET.get('count'):
            count = obj.food.foodingredient_set.values('count')
            return count_nutrition(data, count[0]['count'], 'vit_c')
        return data

    class Meta:
        model = FoodNutrition
        exclude = ['id']


class FoodSerializer(serializers.ModelSerializer):
    nutrition = serializers.SerializerMethodField()

    def get_nutrition(self, obj):
        data = obj.foodnutrition_set.all()
        return FoodNutritionSerializer(instance=data, many=True, context={'request': self.context['request']}).data

    class Meta:
        model = Food
        fields = ('id', 'name', 'kcal', 'nutrition')


#
class FoodIngredientSerializer(serializers.ModelSerializer):
    food = serializers.SerializerMethodField()

    def get_food(self, obj):
        data = Food.objects.filter(name=obj.food.name)
        return FoodSerializer(instance=data, many=True, context={'request': self.context['request']}).data

    class Meta:
        model = FoodIngredient
        exclude = []


class RecipeSerializers(serializers.ModelSerializer):
    step = serializers.SerializerMethodField()
    ingredients = serializers.SerializerMethodField()

    def get_step(self, obj):
        return obj.step.values('step')

    def get_ingredients(self, obj):
        data = obj.ingredients.all()
        return FoodIngredientSerializer(instance=data, many=True, context={'request': self.context['request']}).data

    def to_representation(self, instance):
        ret = super(RecipeSerializers, self).to_representation(instance)
        lens = len(ret['ingredients'])
        ret['kcal_total'] = 0
        ret['protein_total'] = 0
        ret['lemak_total'] = 0
        ret['karbo_total'] = 0
        for y in range(lens):
            ret['kcal_total'] += ret['ingredients'][y]['food'][0]['kcal']
            ret['protein_total'] += float(ret['ingredients'][y]['food'][0]['nutrition'][0]['protein'].split(' ')[0])
            ret['lemak_total'] += float(ret['ingredients'][y]['food'][0]['nutrition'][0]['lemak'].split(' ')[0])
            ret['karbo_total'] += float(ret['ingredients'][y]['food'][0]['nutrition'][0]['carbo'].split(' ')[0])
        return ret

    class Meta:
        model = Recipe
        exclude = []
