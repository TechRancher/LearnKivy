from kivymd.app import MDApp
from kivy.lang import Builder 
import sqlite3

class SQL_db_App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create Database or Connect to one
        conn = sqlite3.connect("first_db.db")

        # Create Cursor
        c = conn.cursor()

        # Create Table
        c.execute("""CREATE TABLE IF NOT EXISTS customers (
            first_name text
        )""")

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        return Builder.load_file("sqldb.kv")
    

    
    def submit(self):
        # Create Database or Connect to one
        conn = sqlite3.connect("first_db.db")

        # Create Cursor
        c = conn.cursor()

        # Add Record
        c.execute("INSERT INTO customers VALUES (:first_name)",
        {
            "first_name": self.root.ids.word_input.text,
        })

        # Add a little message
        self.root.ids.word_label.text = f"{self.root.ids.word_input.text} Added!"

        # Clear the input box
        self.root.ids.word_input.text = ""

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    def show_records(self):
         # Create Database or Connect to one
        conn = sqlite3.connect("first_db.db")

        # Create Cursor
        c = conn.cursor()

        # Query the Database
        c.execute("SELECT * FROM customers")
        records = c.fetchall()

        # variable to hold records
        word = ""
        # Loop thru records
        for record in records:
            word = f"{word}\n {record[0]}"
            # Show 
            self.root.ids.word_label.text = f"{word}"

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()
    
SQL_db_App().run()