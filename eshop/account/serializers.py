from rest_framework.serializers import ModelSerializer

from account.models import User


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
