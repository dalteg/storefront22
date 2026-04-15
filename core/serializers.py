from djoser.serializers  import UserCreateSerializer as BaserUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers 


class UserCreateSerializer(BaserUserCreateSerializer):
    class Meta(BaserUserCreateSerializer.Meta):
        fields =  ['id','username', 'password',
                   'email','first_name', 'last_name']
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields =  ['id','username', 'email','first_name', 'last_name']