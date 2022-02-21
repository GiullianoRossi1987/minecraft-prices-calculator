from django.test import TestCase
from .models import Sell

class DynamicPricesTest(TestCase):
	
	def setUp(self):
		"""
		Sets the dinamic prices test table to test the view method of the table
		it adds 3 sell logs of oak logs used only for testing. The average dynamic price
		of the logs in copper should be 1
		1 - oak_log | 1 | 10 copper | actual datetime
		2 - oak_log | 2 | 20 copper | actual datetime
		3 - oak_log | 1 | 10 copper | actual datetime
		"""
		
		Sell.objects.create(cd=1, item="oak_log", qtd=1, value=10)
		Sell.objects.create(cd=2, item="oak_log", qtd=2, value=20)
		Sell.objects.create(cd=3, item="oak_log", qtd=1, value=10)
	

	def test_insert(self):
		"""
		Checks if the setup proccess was successful
		"""
		self.assertEqual(Sell.get_count(), 3)
	
	def test_exists(self):
		"""
		Checks if the item_exists method is working
		"""
		self.assertEqual(Sell.item_exists("oak_log"), True)
	
	def test_avg(self):
		"""
		Checks if the get_avg_dynamic_price is working well
		using the data from the setup
		"""
		self.assertEqual(Sell.get_avg_dynamic_price("oak_log"), 10)

	
	
	
	

