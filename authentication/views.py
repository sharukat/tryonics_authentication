from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login
#from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
#from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([JWTAuthentication])
def hello_world(request):
    return HttpResponse("Hello World!")

