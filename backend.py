import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO inventory VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM inventory")
        rows = self.cur.fetchall()
        return rows

    def search(self, title = "", author = "", year = "",isbn = ""):
        self.cur.execute("SELECT * FROM inventory WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM inventory WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE inventory SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()




#insert("Star Light", " M.Gaba", 1960, 134567892)
#delete(3)
#update(5, "Life's Beautiful", "Anthony Robbins", 1920, 123456789)
#print(view())
#print(search(author = "W.Smith"))
