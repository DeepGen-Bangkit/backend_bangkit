from django.conf import settings
from rest_framework import serializers
from food.models import Food, FoodNutrition, Recipe, FoodIngredient
from food.utils import count_nutrition, count_presentation, convert_mg_to_g


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

    def count_data(self, obj, nutrition, name):
        if self.context['request'].GET.get('count'):
            if 'recipe' in self.context['request'].get_full_path():
                count = obj.food.foodingredient_set.values('count')
                return count_nutrition(nutrition, count[0]['count'], name)
            else:
                return count_nutrition(nutrition, 100, name)

    def get_carbo(self, obj):
        data = obj.carbo
        return self.count_data(obj, data, 'carbo')

    def get_protein(self, obj):
        data = obj.protein
        return self.count_data(obj, data, 'protein')

    def get_lemak(self, obj):
        data = obj.lemak
        return self.count_data(obj, data, 'lemak')

    def get_air(self, obj):
        data = obj.air
        return self.count_data(obj, data, 'air')

    def get_energi(self, obj):
        data = obj.energi
        return self.count_data(obj, data, 'energi')

    def get_serat(self, obj):
        data = obj.serat
        return self.count_data(obj, data, 'serat')

    def get_abu(self, obj):
        data = obj.abu
        return self.count_data(obj, data, 'abu')

    def get_kalsium(self, obj):
        data = obj.kalsium
        return self.count_data(obj, data, 'kalsium')

    def get_fosfor(self, obj):
        data = obj.fosfor
        return self.count_data(obj, data, 'fosfor')

    def get_natrium(self, obj):
        data = obj.natrium
        return self.count_data(obj, data, 'natrium')

    def get_besi(self, obj):
        data = obj.besi
        return self.count_data(obj, data, 'besi')

    def get_kalium(self, obj):
        data = obj.kalium
        return self.count_data(obj, data, 'kalium')

    def get_tembaga(self, obj):
        data = obj.tembaga
        return self.count_data(obj, data, 'tembaga')

    def get_seng(self, obj):
        data = obj.seng
        return self.count_data(obj, data, 'seng')

    def get_retinol(self, obj):
        data = obj.retinol
        return self.count_data(obj, data, 'retinol')

    def get_b_kar(self, obj):
        data = obj.b_kar
        return self.count_data(obj, data, 'b_kar')

    def get_kar_total(self, obj):
        data = obj.kar_total
        return self.count_data(obj, data, 'kar_total')

    def get_thiamin(self, obj):
        data = obj.thiamin
        return self.count_data(obj, data, 'thiamin')

    def get_riboflavin(self, obj):
        data = obj.riboflavin
        return self.count_data(obj, data, 'riboflavin')

    def get_niasin(self, obj):
        data = obj.niasin
        return self.count_data(obj, data, 'niasin')

    def get_vit_c(self, obj):
        data = obj.vit_c
        return self.count_data(obj, data, 'vit_c')

    class Meta:
        model = FoodNutrition
        exclude = ['id']


class FoodSerializer(serializers.ModelSerializer):
    nutrition = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url

    def get_nutrition(self, obj):
        data = obj.foodnutrition_set.all()
        return FoodNutritionSerializer(instance=data, many=True, context={'request': self.context['request']}).data

    class Meta:
        model = Food
        fields = ('id', 'name', 'kcal', 'nutrition', 'image')


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
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url

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
        total_nutrition = 0
        #total_nutrition += convert_mg_to_g(key, count_nutritions[key].split(' ')[0])
        for y in range(lens):
            for key, value in ret['ingredients'][y]['food'][0]['nutrition'][0].items():
                if key not in ['id', 'food']:
                    total_nutrition += convert_mg_to_g(key, value)
            ret['kcal_total'] += ret['ingredients'][y]['food'][0]['kcal']
            ret['protein_total'] += float(ret['ingredients'][y]['food'][0]['nutrition'][0]['protein'].split(' ')[0])
            ret['protein_presentase'] += count_presentation(ret['protein_total'], total_nutrition)
            ret['lemak_total'] += float(ret['ingredients'][y]['food'][0]['nutrition'][0]['lemak'].split(' ')[0])
            ret['lemak_presentase'] += count_presentation(ret['lemak_total'], total_nutrition)
            ret['karbo_total'] += float(ret['ingredients'][y]['food'][0]['nutrition'][0]['carbo'].split(' ')[0])
            ret['karbo_presentase'] += count_presentation(ret['karbo_total'], total_nutrition)
        return ret

    class Meta:
        model = Recipe
        exclude = []
