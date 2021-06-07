from django.shortcuts import render

# Create your views here.
from oxy_info.models import Place
from oxy_info.serializers import PlaceSerializer
from rest_framework import generics

class PlaceList(generics.ListCreateAPIView):
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer

