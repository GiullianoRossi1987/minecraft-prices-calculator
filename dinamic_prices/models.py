from django.db import models
from decimal import Decimal

class Sell(models.Model):
	"""
	"""
	cd = models.IntegerField(primary_key=True)
	item = models.TextField()
	qtd = models.IntegerField()
	value = models.DecimalField(max_digits=10, decimal_places=2)
	datetime_sell = models.DateTimeField()




