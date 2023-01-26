from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=8, write_only=True)

    '''
    The `UserSerializer` class defines a `password` field, 
    which is a `CharField` with a minimum length of 8 characters. 
    The `write_only` argument is set to `True`, 
    which means that the password field will only be used when writing data to the serializer but will not be included in the serialized output since we do not want the password to be compromised.
    '''

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        '''
        The `Meta` class within the `UserSerializer` class specifies the `model` that the serializer should be used for (in this case, the `User` model), 
        and the list of `fields` that should be included in the serialized output. 
        In this case, the `username`, `email`, and `password` fields will be included in the serialized output.
        '''

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
