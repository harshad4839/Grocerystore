from django.urls import path
from .views import Menu_list,Menu_detail

urlpatterns = [
    path('menuview/',Menu_list),
    path('menulist/<int:pk>/',Menu_detail)
]