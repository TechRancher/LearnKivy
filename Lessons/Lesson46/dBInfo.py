import psycopg2

class Database:
    def __init__(self):
        # Create Database or Connect to one
        self.conn = psycopg2.connect(
            host="host",
            port="2345",
            user="user",
            password="password",
            database="myDB",
        )

        # Create Cursor
        self.c = self.conn.cursor()

    def create_table(self):
        # Create Table
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS todo_list (
            title VARCHAR(75), date DATE, description VARCHAR(255), done BOOLEAN
        )"""
        )

        # Commit Changes
        self.conn.commit()

    def close_connection(self):
        # Close Connection
        self.conn.close()
