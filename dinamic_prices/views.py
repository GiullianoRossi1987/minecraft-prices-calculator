from django.shortcuts import render
from rest_framework import viewsets
from .models import Sell
from .serializers import SellSerializer
from json import dump
# from django.http import HttpResponse, JsonResponse

class SellViewSet(viewsets.ModelViewSet):
	"""
	"""

	queryset = Sell.objects.all()
	serializer_class = SellSerializer

def index(request):
	"""
	The application's main page, it'll have the data about the prices and the averages 
	"""

	return render(request, "dp/index.html", {"sells": Sell.all_dict()})



