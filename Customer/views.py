from django.shortcuts import render
from Owner.models import Menu
from Owner.serializers import MenuSerializer
from .models import Cart
from .serializers import CartSerializer
from .models import Customer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def stocks(request):
    if request.method == 'GET':
        Menus=Menu.objects.all()
        serializer = MenuSerializer(Menus, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def customercartview(request):
    if request.method == 'GET':
        carts=Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def customercartlist(request, pk):
    try:
        carts = Cart.objects.get(pk=pk)

    except cart.DoesnotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CartSerializer(carts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CartSerializer(carts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        carts.delete()
        carts.active_status=False
        carts.save
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['POST'])
def customer_login(request):
    if request.method == 'POST':
        try:
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)

            customer = Customer.objects.get(user=user)
            if customer.active_status == True:
                if customer.enabled_status == True:
                    refresh = RefreshToken.for_user(user)
                    data = {}
                    data.update( {'refresh': str(refresh) })
                    data.update( {'access': str(refresh.access_token)})
                    return Response(data)
                else:
                    return Response({'app_data':'This customer is a revoked user'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'app_data':'This customer is a deleted user'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as E:
            return Response({'app_data':'Something went wrong', 'dev_data':str(E)}, status=status.HTTP_400_BAD_REQUEST)


