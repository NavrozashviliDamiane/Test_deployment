from django.shortcuts import render
from django.contrib.auth import get_user_model 
from rest_framework import generics
from .serializers import (
		PizzeriaListSerializer, 	
	)
    
from .models import Pizzeria
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
# Create your views here.


class PizzeriaListAPIView(generics.ListAPIView):
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaListSerializer




		