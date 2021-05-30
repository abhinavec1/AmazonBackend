from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DecimalField
from phonenumber_field.modelfields import PhoneNumberField
from meds.models import MedList

class ShopOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(MedList ,through='Stock')
    phoneNum = PhoneNumberField()
    latitude = DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    longitude = DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    rating = models.DecimalField(decimal_places=1, max_digits=2, default=0.0)

    def __str__(self):
        return self.user.first_name

class Stock(models.Model):
    storeOwner = models.ForeignKey(ShopOwner, on_delete=models.CASCADE)
    medName = models.ForeignKey(MedList, on_delete=models.CASCADE)
    medQnty = models.IntegerField()

    def  __str__(self):
        return str(self.storeOwner.user.first_name) + ' [ ' + str(self.medName.name) + ',' + str(self.medQnty) + ' ]'