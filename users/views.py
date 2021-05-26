from django.shortcuts import render

# Create your views here.
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_framework import status
from rest_framework.response import Response


class CustomLoginView(LoginView):
    pass


class CustomRegisterView(RegisterView):

    def create(self, request, *args, **kwargs):
        super(CustomRegisterView, self).create(request, *args, **kwargs)
        ret = {
            "msg": "success"
        }
        return Response(ret)
