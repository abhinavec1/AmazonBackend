from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from meds.models import MedList

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNum = PhoneNumberField()

    def __str__(self):
        return self.user.first_name


class Request(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    medName = models.ForeignKey(MedList, on_delete=models.CASCADE)
    medQnty = models.PositiveIntegerField()
    completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now=True)   
    time_created = models.TimeField(auto_now=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)

    def __str__(self):
        return str(self.customer.user.first_name) + ' [ ' + str(self.medName.name) + ',' + str(self.medQnty) + ' ]'


@receiver(post_save, sender=User)
def post_save_create_token(sender, created=False, instance=None, **kwargs):
    if created:
        Token.objects.create(user=instance)
# Create your models here.
