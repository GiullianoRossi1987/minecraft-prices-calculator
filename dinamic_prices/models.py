from django.db import models
from decimal import Decimal

class Sell(models.Model):
	"""
	"""
	cd = models.IntegerField(primary_key=True)
	item = models.TextField()
	qtd = models.IntegerField()
	value = models.DecimalField(max_digits=10, decimal_places=2)
	datetime_sell = models.DateTimeField(auto_now_add=True, blank=True)

	class ItemSellNotFound(Exception):
		"""
		Raised when the table tries to access the sell logs of an item that
		doesn't exist
		"""

		def __init__(self, item: str):
			super(f"Item \"{item}\" not found in the sell logs")

	@staticmethod
	def item_exists(needle: str) -> bool:
		"""
		Verifies if there's any sell logs of an item
		"""

		result = (Sell.objects
			.values("item")
			.annotate(occourences=models.Count("item"))
			.filter(item=needle)
		)
		return result.all()[0]["occourences"] > 0
	
	@staticmethod
	def get_count() -> int:
		"""
		DEBUG ONLY TOOL
		Counts all the logs in the table
		"""
		result = (Sell.objects
			.values("item")
			.annotate(icount=models.Count("item"))
		)
		return result.all()[0]["icount"]


	def get_avg_dynamic_price(self, item: str):
		"""
		
		"""

