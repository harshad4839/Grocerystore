from django.urls import path
from .views import stocks
from .views import customercartlist,customercartview,customer_login

urlpatterns = [
    path('stocks/',stocks),
    path('cartlist/<int:pk>/',customercartlist),
    path('cartview/', customercartview),
    path('customerlogin/',customer_login),


]