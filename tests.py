from lib.database.Connection import Connection

con = Connection()
c = con.get_cursor()
c.execute("SELECT * FROM MPC.MINECRAFT_ITEM;")
