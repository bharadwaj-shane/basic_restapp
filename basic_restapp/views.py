from django.shortcuts import render
from time import sleep
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def defaulturl(request, format=None):
    return Response("Please add extension to url", status=status.HTTP_200_OK)