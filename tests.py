from lib.database.Connection import Connection
from lib.database.entities.Sells import *

con = Sells()
con.add_sell("test", 1, 10)
print([str(x) for x in con.get_sells()])

