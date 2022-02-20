# encoding = UTF-8
# using namespace std
from ..Connection import Connection


class StaticItem:
	"""
	"""

	__cd: int
	__item: str
	__vl_ideal: float
	__is_fuel: bool
	__brute_item: bool

	def __init__(self, data):
		"""
		"""
		self.__cd, self.__item, self.__vl_ideal, self.__is_fuel, self.__brute_item = data
	
	def __str__(self) -> str?
		"""
		"""
		return f"#{self.__cd} '{self.__item}' - {self.__vl_ideal}"
