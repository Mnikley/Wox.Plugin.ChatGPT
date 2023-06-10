import json
import sqlite3


class QueryDB:
    def __enter__(self):
        # Establish a database connection and cursor when entering the context
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

        # Create the 'queries' table if it doesn't exist
        self.cursor.execute("CREATE TABLE IF NOT EXISTS queries "
                            "(id INTEGER PRIMARY KEY,"
                            "input TEXT,"
                            "result TEXT,"
                            "cost REAL,"
                            "config JSON,"
                            "status TEXT)")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the database connection when exiting the context
        self.conn.close()

    def insert_query(self, config):
        # Insert a new query into the 'queries' table
        clean_config = {k: v for k, v in config.items() if k != "api_key"}
        self.cursor.execute("INSERT INTO queries (input, result, cost, config, status) "
                            "VALUES (?, ?, ?, ?, ?)",
                            (clean_config['input_prompt'],
                             clean_config['completion_text'],
                             clean_config['session_spent_text'],
                             json.dumps(clean_config),
                             clean_config['status']))
        self.conn.commit()

    def get_all(self):
        # Retrieve all queries from the 'queries' table
        self.cursor.execute("SELECT * FROM queries ORDER BY id DESC")
        results = self.cursor.fetchall()
        return results

    def get_by_id(self, query_id):
        # Retrieve a specific query by its ID from the 'queries' table
        self.cursor.execute("SELECT * FROM queries WHERE id = ?", (query_id+1,))
        query = self.cursor.fetchone()
        return query
