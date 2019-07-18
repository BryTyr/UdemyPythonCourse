import psycopg2

def create_table():
        conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='127.0.0.1' port='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
        cur.execute("INSERT INTO store VALUES ('glass',6,3.5)")
        conn.commit()
        conn.close()

def insert(item,quantity,price):
        conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='127.0.0.1' port='5432' ")
        cur=conn.cursor()
        cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
        conn.commit()
        conn.close()

def view_table():
        conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='127.0.0.1' port='5432' ")
        cur=conn.cursor()
        cur.execute("SELECT * FROM store")
        rows=cur.fetchall()
        return rows

def delete(item):
        conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='127.0.0.1' port='5432' ")
        cur=conn.cursor()
        cur.execute("DELETE FROM store WHERE item=%s",(item,))
        conn.commit()
        conn.close()

def update(item,quantity,price):
        conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='127.0.0.1' port='5432' ")
        cur=conn.cursor()
        cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
        conn.commit()
        conn.close()

#create_table()
insert("orange",12,8)
print(view_table())
delete("orange")
print(view_table())
insert("orange",12,8)
print(view_table())
update("orange",12,6)
print(view_table())
