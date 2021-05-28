from django.shortcuts import render
from django.db import IntegrityError
from .models import *
from .serializers import ShopOwnerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from meds.models import MedList
from customer.serializers import RequestSerializer
from customer.models import Request

from store_owner import serializers


@api_view(['POST'])
def RegisterStores(request):
    email = request.data['email']
    password = request.data['password']
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    phoneNum = request.data['phoneNum']
    latitude = request.data['latitude']
    longitude = request.data['longitude']
    if not User.objects.filter(username=email).exists() or not User.objects.filter(email=email).exists():
        user = User(username=email, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        ShopOwner.objects.create(user=user, phoneNum = phoneNum, latitude=latitude, longitude=longitude)
        return Response('Successfully registered')
    else:
        return Response('this email already exists')

@api_view(['GET'])
def RequestList(request):
    requests = Request.objects.filter(completed=False).order_by('-time_created')
    print(requests)
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ItemDetail(request, pk):
    item = Request.objects.get(id=pk)
    serializer = RequestSerializer(item)
    return Response(serializer.data)

@api_view(['POST'])
def UpdateStock(request):
    print(request.data)
    owneremail = request.data['owner']
    owner = ShopOwner.objects.get(user__email=owneremail)
    for order in request.data['meds']:
        print(order)
        medName = order['name']
        medQnty = int(order['qnty'])
        try:
            medId = MedList.objects.get(name=medName)
            stock = Stock.objects.get(storeOwner=owner, medName=medId)
            stock.medQnty += medQnty
            stock.save()
            print('Successfully updated')
        except (MedList.DoesNotExist, Stock.DoesNotExist):
            try:
                medId = MedList.objects.create(name=medName)
            except IntegrityError:    
                medId = MedList.objects.get(name=medName)
            Stock.objects.create(storeOwner=owner, medQnty=medQnty, medName=medId)
            print("Successfully Created")


    return Response("request received")
