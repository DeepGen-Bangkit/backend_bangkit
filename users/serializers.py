from django.utils import timezone
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from awal_menyusui.models import Menyusui
from kehamilan.models import Kehamilan
from users.models import User


class CustomLoginSerializer(LoginSerializer):
    email = serializers.CharField(allow_blank=False, required=True)
    password = serializers.CharField(style={
        'input_type': 'password'
    })


class CustomRegisterSerializer(RegisterSerializer):
    type_user = serializers.IntegerField(required=False, write_only=True)
    name = serializers.CharField(required=True, write_only=True)
    date_birth = serializers.DateField(required=True)
    ttl = serializers.DateField(required=False)
    phase = serializers.IntegerField(required=True)
    hpht = serializers.DateField(required=False)
    hpl = serializers.DateField(required=False)
    baby_name = serializers.CharField(required=False)
    ttl_baby = serializers.DateField(required=False)
    gender = serializers.IntegerField(required=False)
    length = serializers.FloatField(required=False)
    weight = serializers.FloatField(required=False)
    lingkar_kepala = serializers.FloatField(required=False)
    is_mpasi = serializers.BooleanField(required=False)
    type = serializers.IntegerField(required=False)

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name'),
            'email': self.validated_data.get('email'),
            'password1': self.validated_data.get('password1'),
            'password2': self.validated_data.get('password2'),
            'phase': self.validated_data.get('phase'),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'date_birth': self.validated_data.get('date_birth'),
            'ttl': self.validated_data.get('ttl', timezone.now().date()),
            'hpht': self.validated_data.get('hpht', timezone.now().date()),
            'hpl': self.validated_data.get('hpl', timezone.now().date()),
            'baby_name': self.validated_data.get('baby_name', ''),
            'ttl_baby': self.validated_data.get('ttl_baby', timezone.now().date()),
            'gender': self.validated_data.get('gender', 0),
            'length': self.validated_data.get('length', 0),
            'weight': self.validated_data.get('weight', 0),
            'lingkar_kepala': self.validated_data.get('lingkar_kepala', 0),
            'is_mpasi': self.validated_data.get('is_mpasi', False)
        }

    def custom_signup(self, request, user):
        user.date_birth = self.get_cleaned_data()['date_birth']
        user.phase = self.get_cleaned_data()['phase']
        user.username = self.get_cleaned_data()['email']
        user.save()
        if user.phase == 1 or user.phase == 2:
            data = {
                "user": user,
                "baby_name": self.get_cleaned_data()['baby_name'],
                "ttl_baby": self.get_cleaned_data()['ttl_baby'],
                "gender": self.get_cleaned_data()['gender'],
                "length": self.get_cleaned_data()['length'],
                "weight": self.get_cleaned_data()['weight'],
                "lingkar_kepala": self.get_cleaned_data()['lingkar_kepala']
            }
            if user.phase == 1:
                data['is_mpasi'] = False
            else:
                data['is_mpasi'] = True
            Menyusui.objects.create(**data)
        else:
            Kehamilan.objects.create(user=user,
                                     hpl=self.get_cleaned_data()['hpl'],
                                     hpht=self.get_cleaned_data()['hpht'],
                                     ttl=self.get_cleaned_data()['ttl'])
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    kehamilan = serializers.SerializerMethodField(read_only=True)
    menyusui = serializers.SerializerMethodField(read_only=True)
    mpasi = serializers.SerializerMethodField(read_only=True)
    phase = serializers.CharField(source='get_phase_display')

    def get_kehamilan(self, obj):
        try:
            data = Kehamilan.objects.get(user=obj)
        except Kehamilan.DoesNotExist:
            return []
        return []

    def get_menyusui(self, obj):
        try:
            data = Menyusui.objects.get(user=obj, is_mpasi=False)
        except Menyusui.DoesNotExist:
            return []
        return []

    def get_mpasi(self, obj):
        try:
            data = Menyusui.objects.get(user=obj, is_mpasi=True)
        except Menyusui.DoesNotExist:
            return []
        return []

    class Meta:
        model = User
        fields = ['pk', 'name', 'email', 'kehamilan', 'menyusui', 'mpasi', 'phase']
