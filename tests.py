from lib.database.Connection import Connection
from lib.database.entities.Prices import *

con = Prices()
print([str(x) for x in con.get_prices()])

