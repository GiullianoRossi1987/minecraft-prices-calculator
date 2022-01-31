# encoding = UTF-8
# using namespace std

import psycopg2 as psql


class Connection:
	"""
	"""

	__DB = "minecraft_calculator"
	__HOST = "localhost"
	__USER = "mpc_acc"
	__PASS = "mpc_acc"

	_connection = None
	_got_connection = False

	def __init__(self):
		"""
		"""
		self._connection = psql.connect(
			database = self.__DB,
			user     = self.__USER,
			password = self.__PASS,
			host     = self.__HOST
		)
		self._got_connection = True
	
	def __del__(self):
		"""
		"""
		if self._got_connection:
			self._connection.commit()
			self._connection.close()

	def __enter__(self):
		"""
		"""
		if not self._got_connection:
			self._connection = psql.connect(
				database = self.__DB,
				user     = self.__USER,
				password = self.__PASS,
				host     = self.__HOST
			)
			self._got_connection = True
	
	def __exit__(self):
		"""
		"""
		self._connection.commit()
		self._connection.close()
	
	def get_cursor(self):
		"""
		"""
		if self._got_connection:
			cursor = self._connection.cursor()
			return cursor

		

