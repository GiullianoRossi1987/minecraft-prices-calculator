from django.shortcuts import render
from .models import Sell
from json import dump
# from django.http import HttpResponse, JsonResponse

def index(request):
	"""
	The application's main page, it'll have the data about the prices and the averages 
	"""

	return render(request, "dp/index.html", {"sells": Sell.all_dict()})

