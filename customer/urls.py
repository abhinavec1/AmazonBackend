from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.RegisterUsers, name="register"),
    path('list/', views.RequestList, name="request-list"),
    path('create-request/', views.CreateRequest, name="create-request"),
    path('search-meds/', views.SearchMeds, name="search-meds"),
    path('login/', obtain_auth_token, name="login"),
    path('logindetails/', views.LoginUser),
    path('getmedlist/', views.GetMedList)
]