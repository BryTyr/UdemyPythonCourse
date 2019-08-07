import sqlite3

class Database:

    def __init__(self,db):
        self.connection=sqlite3.connect(db)
        self.cur=self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text, year integer, isbn integer)")
        self.connection.commit()


    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.connection.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows


    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.connection.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.connection.commit()


    def __del__():
        self.connection.close()

        
#insert("globes","sam blog",1990,913323332)
#insert("joe blogs","joe blog",2000,813323332)
#print(view())
#update(4,"joe blogs","stephen blog",2000,813323332)
#print(search(author="sam blog"))
#delete(2)
#print(view())
