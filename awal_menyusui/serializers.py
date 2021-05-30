from rest_framework import serializers
from awal_menyusui.models import Menyusui


class MenyusuiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menyusui
        exclude = ['id']
