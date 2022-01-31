#encoding = UTF-8
#using namespace std
from ..Connection import Connection
from typing import Tuple

class Price:
	"""
	"""

	item: str = ""
	price: float = 0.0

	def __init__(self, data):
		"""
		"""
		self.item = data[0]
		self.price = data[1]
	
	def __str__(self) -> str:
		"""
		"""
		return f"{self.item} : {self.price}"
	
	def __tuple__(self) -> tuple:
		"""
		"""
		return (self.item, self.price)
	

class Prices(Connection):
	"""
	"""
	_hdl = None

	def __init__(self):
		super().__init__()
		self._hdl = self.get_cursor()
	
	def get_prices(self) -> Tuple[Price]:
		"""
		"""
		self._hdl.execute("SELECT * FROM MPC.AGV_PRICES;")
		fall = self._hdl.fetchall()
		return tuple(Price(x) for x in fall)
	
	def get_price_of(self, item: str):
		"""
		"""
		self._hdl.execute("SELECT * FROM MPC.AGV_PRICES WHERE ITEM = %s", (item))
		fone = self._hdl.fetchone()
		return Price(fone)
	

