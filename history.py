import json
import sqlite3


class QueryDB:
    def __init__(self):
        self.conn = ''
        self.cursor = ''
        self.connect()

    def connect(self):
        # connect to db, if not exist, will create
        self.conn = sqlite3.connect('database.db')
        # create cursor
        self.cursor = self.conn.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS queries "
                            "(id INTEGER PRIMARY KEY,"
                            "input TEXT,"
                            "result TEXT,"
                            "cost REAL,"
                            "config JSON,"
                            "status TEXT)")

    def insert_query(self, config):
        if not self.conn or not self.cursor:
            self.connect()

        del config['api_key']
        self.cursor.execute("INSERT INTO queries (input, result, cost, config, status) "
                            "VALUES (?, ?, ?, ?, ?)",
                            (config['input_prompt'],
                             config['completion_text'],
                             config['session_spent_text'],
                             json.dumps(config),
                             config['status']))
        self.conn.commit()
        self.conn.close()

    def get_all(self):
        if not self.conn or not self.cursor:
            self.connect()

        self.cursor.execute("SELECT * FROM queries ORDER BY id DESC")
        results = self.cursor.fetchall()
        self.conn.close()

        return results

    def get_by_id(self, query_id):
        if not self.conn or not self.cursor:
            self.connect()
        self.cursor.execute("SELECT * FROM queries WHERE id = ?", (query_id+1,))
        query = self.cursor.fetchone()
        self.conn.close()

        return query
