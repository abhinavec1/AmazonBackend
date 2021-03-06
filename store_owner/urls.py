from django.urls import path
from . import views

urlpatterns = [
    path('register-store/', views.RegisterStores, name="register-store"),
    path('list/', views.RequestList, name="owner-list"),
    path('update-stock/', views.UpdateStock, name="update-stock"),
    path('item-detail/<str:pk>/', views.ItemDetail, name="item-detail"),
    path('completereq/<str:pk>', views.CompleteReq),
    path('offlinereq/', views.OfflineReq),
]