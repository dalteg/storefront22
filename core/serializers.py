from djoser.serializers import UserCreateSerializer as  BaserUserCreateSerializer
from rest_framework import serializers


class UserCreateSerializer(BaserUserCreateSerializer):
    class Meta(BaserUserCreateSerializer.Meta):
        fields =  ['id','username', 'password',
                   'email','first_name', 'last_name']
