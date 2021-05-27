from rest_framework import serializers
from .models import *
from customer.serializers import UserSerializer

class ShopOwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ShopOwner
        fields = ['user', 'phoneNum', 'latitude', 'longitude']

