from rest_framework import serializers
from kehamilan.models import Kehamilan


class KehamilanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kehamilan
        exclude = ['id']
