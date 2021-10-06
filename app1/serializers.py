from rest_framework import serializers
from app1.models import *

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=ajaxex
        fields=('id','name','address','email')
