"""
No comments for this one since the function/method names
and SQL commands read so much like English.
"""
import sqlite3


class Database:

	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, entry text)")
		self.conn.commit()

	def insert(self, entry):
		self.cur.execute("INSERT INTO book VALUES (NULL, ?)", (entry,))
		self.conn.commit()

	def view(self):
		self.cur.execute("SELECT * FROM book")
		rows = self.cur.fetchall()
		return rows

	def delete(self, id):
		self.cur.execute("DELETE FROM book WHERE id=?", (id, ))
		self.conn.commit()

	def update(self, id, entry):
		self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (entry, id))
		self.conn.commit()

	def __del__(self):
		self.conn.close()
