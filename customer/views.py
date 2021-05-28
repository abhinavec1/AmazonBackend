from django.contrib.auth.models import UserManager
from store_owner.models import Stock
from django.shortcuts import render
from .models import *
from store_owner.serializers import ShopOwnerSerializer
from .serializers import RequestSerializer ,MedNameSerializer
from meds.models import MedList
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.authtoken.views import obtain_auth_token

from customer import serializers



@api_view(['POST'])
def RegisterUsers(request):
    email = request.data['email']
    password = request.data['password']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    phoneNum = request.data['phoneNum']
    if not User.objects.filter(username=email).exists() or not User.objects.filter(email=email).exists():
        user = User(username=email, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        Customer.objects.create(user=user, phoneNum = phoneNum)
        return Response('Successfully registered')

    else:
        return Response('this email already exists')

@api_view(['POST'])
def LoginUser(request):
    username = request.data['username']
    name = User.objects.get(username=username).first_name
    phoneNum = str(Customer.objects.get(user__username=username).phoneNum)
    data =  {'name': name, 'phoneNum': phoneNum}
    return Response(data)

@api_view(['POST'])
def RequestList(request):
    requests = Request.objects.filter(customer__user__email = request.data['email'])
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateRequest(request):
    medName = request.data['medName']
    latitude = request.data['latitude']
    longitude = request.data['longitude']
    try:
        medName = MedList.objects.get(name=medName)
    except MedList.DoesNotExist:
        medName = MedList.objects.create(name=medName)
    medQnty = int(request.data['medQnty'])
    customer = Customer.objects.get(user__email = request.data['email'])
    try:
        request = Request.objects.get(customer=customer, medName=medName)
        if request.completed == False:
            return Response('Order already exists')
        else:
            request = Request.objects.create(customer=customer, medName=medName, medQnty=medQnty, latitude=latitude, longitude=longitude)
            return Response('Request generated')
    except Request.DoesNotExist:
        request = Request.objects.create(customer=customer, medName=medName, medQnty=medQnty, latitude=latitude, longitude=longitude)
        return Response('Request generated')

@api_view(['POST'])
def SearchMeds(request):
    medName = request.data['medName']
    try:
        medName = MedList.objects.get(name=medName)
    except MedList.DoesNotExist:
        return Response('Medicine is not available')
    medQnty = int(request.data['medQnty'])
    stocks = Stock.objects.filter(medName=medName, medQnty__gte = medQnty)
    shopowners = []
    for stock in stocks:
        shopowners.append(stock.storeOwner)    
    if len(shopowners) == 0:
        return Response(str(medName.name) + ' is not available in the desired quantity')
    serializer = ShopOwnerSerializer(shopowners, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GetMedList(request):
    medicines = MedList.objects.all()
    serializer = MedNameSerializer(medicines, many=True)
    return Response(serializer.data)
