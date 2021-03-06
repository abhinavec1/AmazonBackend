from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from meds.models import MedList

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = ['user', 'phoneNum']

class MedNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedList
        fields = ['name']

class RequestSerializer(serializers.ModelSerializer): ### Update this to give email and phone number only if not used any where else
    customer = CustomerSerializer()
    medName = MedNameSerializer()
    class Meta:
        model = Request
        fields = ['id', 'medQnty', 'medName', 'completed', 'date_created', 'time_created', 'customer']

class MedReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedList
        fields = '__all__'
        

