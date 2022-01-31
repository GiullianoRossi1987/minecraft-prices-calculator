#encoding = UTF-8
#using namespace std
from ..Connection import Connection
from typing import Type, List, Tuple

class Item:
	"""
	"""
	
	cd: int = 0
	nm: str = ""
	work_l: int
	work_c: int
	value: int # vl_ideal

	def __init__(self, data):
		"""
		"""
		self.cd     = data[0]
		self.nm     = data[1]
		self.work_l = data[2]
		self.work_c = data[3]
		self.value  = data[4]
	
	def flush(self):
		self.cd     = 0
		self.nm     = ""
		self.work_l = 0
		self.work_c = 0
		self.value  = 0
	
	def __del__(self):
		self.flush();
	
	@staticmethod
	def calc_vl_ideal(work_c, work_l): return work_c * (work_l - 62)  # IDEAL VALUE OF THE ITEM 
	
	@staticmethod
	def calc_vl_sell(vl_ideal, n_gov = 0, n_buyer = 0): return vl_ideal + (n_gov + n_buyer) # VALUE OF THE SELL ITSELF
	
	def update_vl(self):
		self.value = Item.calc_vl_ideal(self.work_c, self.work_l)
	

class ItemHandler(Connection):
	"""
	"""

	__hdl_cursor = None

	def __init__(self):
		"""
		"""
		super()
		self.__hdl_cursor = self.get_cursor()
	
	def get_items(self) -> Tuple[Item]:
		"""
		"""
		self.__hdl_cursor.execute("SELECT * FROM MPC.MINECRAFT_ITEM;")
		fall = self.__hdl_cursor.fetchall()
		return tuple(map(fall, lambda x: Item(x)))
