from django.conf import settings
from django.shortcuts import render

# Create your views here.
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_framework import status
from rest_framework.response import Response

from users.models import User


class CustomLoginView(LoginView):

    def get_response(self):
        serializer_class = self.get_response_serializer()
        data = {
            'user': self.user,
            'token': self.token
        }
        serializer = serializer_class(instance=data, context={'request': self.request})
        data = serializer.data
        data['message'] = "Success"
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        # Check whether the email provided is a registered user
        try:
            user = User.objects.get(email__iexact=self.request.data['email'])
        except User.DoesNotExist:
            return Response({
                'non_field_errors': ['User is not registered. Please register for a new account']
            }, status=400)
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()


class CustomRegisterView(RegisterView):

    def create(self, request, *args, **kwargs):
        super(CustomRegisterView, self).create(request, *args, **kwargs)
        ret = {
            "msg": "success"
        }
        return Response(ret)
