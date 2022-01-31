#encoding = UTF-8
#using namespace std
from ..Connection import Connection
from typing import Type, List, Tuple

class SellLog:
	"""
	"""

	__cd: int = 0
	item: str = ""
	currency: float = 0.0
	qt_itens: int = 1
	dt = None   # datetime

	def __init__(self, data):
		"""
		"""
		self.__cd     = data[0]
		self.item     = data[1]
		self.qt_itens = data[2]
		self.currency = data[3]
		self.dt       = data[4]
	
	def get_currency_item(self) -> float:
		"""
		"""
		return self.currency/self.qt_itens
	
	def get_cod(self) -> int: return self.__cd
	
	def __str__(self) -> str:
		"""
		"""
		return f"#{self.__cd} ITEM: {self.item} [{self.qt_itens}] => R$ {self.currency}"
	
	def __tuple__(self) -> tuple:
		"""
		"""
		return (self.__cd, self.item, self.currency, self.qt_itens, self.dt)
	
	def __dict__(self) -> dict:
		"""
		"""
		return {
			"CD": self.__cd,
			"NM": self.item,
			"QTD": self.qt_itens,
			"VL_CURRENCY": self.currency,
			"DT_TM_SELL": self.dt
		}
	
	def insert_tuple(self) -> tuple:
		"""
		"""
		return (self.item, self.qt_itens, self.currency)

class Sells(Connection):
	"""
	"""

	_hdl = None

	def __init__(self):
		"""
		"""
		super().__init__()
		self._hdl = self.get_cursor()
	
	def get_sells(self) -> Tuple[SellLog]:
		"""
		"""
		self._hdl.execute("SELECT * FROM MPC.SELLS;")
		fall = self._hdl.fetchall()
		return tuple([SellLog(x) for x in fall])
	
	def add_sell(self, item: str, qt: int, currency: float):
		"""
		"""
		self._hdl.execute("INSERT INTO MPC.SELLS (ITEM, QTD, VL_CURRENCY) VALUES (%s, %s, %s);", (item, qt, currency))
		self._connection.commit()

	
	
	



	
	

