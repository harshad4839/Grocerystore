from django.shortcuts import render


from django.http import HttpResponse,JsonResponse

from .models import Menu
from .serializers import MenuSerializer

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Menu_list(request):
    if request.method == 'GET':
        Menus=Menu.objects.all()
        serializer = MenuSerializer(Menus, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view([ 'GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def Menu_detail(request, pk):
    try:
        menu = Menu.objects.get(pk=pk)

    except Menu.DoesnotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuSerializer(menu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        menu.delete()
        menu.active_status = False
        menu.save
        return Response(status=status.HTTP_204_NO_CONTENT)



