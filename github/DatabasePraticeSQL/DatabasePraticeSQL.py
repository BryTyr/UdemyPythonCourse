import sqlite3

def create_table():
        conn=sqlite3.connect('lite.db')
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
        cur.execute("INSERT INTO store VALUES ('glass',6,3.5)")
        conn.commit()
        conn.close()

def insert(item,quantity,price):
        conn=sqlite3.connect('lite.db')
        cur=conn.cursor()
        cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
        conn.commit()
        conn.close()

def view_table():
        conn=sqlite3.connect('lite.db')
        cur=conn.cursor()
        cur.execute("SELECT * FROM store")
        rows=cur.fetchall()
        return rows

def delete(item):
        conn=sqlite3.connect('lite.db')
        cur=conn.cursor()
        cur.execute("DELETE FROM store WHERE item=?",(item,))
        conn.commit()
        conn.close()

def update(item,quantity,price):
        conn=sqlite3.connect('lite.db')
        cur=conn.cursor()
        cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
        conn.commit()
        conn.close()

insert("wine glass",12,8)
update("water glass",10,6)
print(view_table())
delete("wine glass")
print(view_table())
update("water glass",11,7)
print(view_table())
