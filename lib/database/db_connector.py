import sqlite3

class DBConnector:
    def __init__(self):
        self.conn = sqlite3.connect('pinet_manager.db')
        self.cursor = self.conn.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
