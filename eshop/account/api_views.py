from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet

from account.models import User
from account.serializers import LoginSerializer


class LoginView(ModelViewSet):
    serializer_class= LoginSerializer
    queryset=User.objects.all()

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }
    def post(self,request):
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = authenticate(phone_number=phone_number, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            return self._error_response('disabled')
        return self._error_response('invalid')