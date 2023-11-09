from django.shortcuts import render
from rest_framework import viewsets

from . models import Clothes
from .serializers import ProductSerializer


# Create your views here.

class Products(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ProductSerializer

