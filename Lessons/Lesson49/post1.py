from kivymd.app import MDApp
from kivy.lang import Builder 
import psycopg2

class Postges_db_App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create Database or Connect to one
        conn = psycopg2.connect(
            host = "host",
            port = "2345",
            user = "user",
            password = "password",
            database = "database",

        )

        # Create Cursor
        c = conn.cursor()

        # Create Database
        # We do not need to create a database because we already have one that was created in pgAdmin

        # Create Table
        c.execute("""CREATE TABLE IF NOT EXISTS customers (
            first_name VARCHAR(75);
        )""")

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        return Builder.load_file("post1.kv")
    

    
    def submit(self):
         # Create Database or Connect to one
        conn = psycopg2.connect(
            host = "host",
            port = "2345",
            user = "user",
            password = "password",
            database = "database",

        )

        # Create Cursor
        c = conn.cursor()

        # Add A Record
        sql_command = "INSERT INTO customers (first_name)VALUES (%s)"
        values = (self.root.ids.word_input.text,)

        # Execute Command
        c.execute(sql_command, values)

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
        conn = psycopg2.connect(
            host = "host",
            port = "2345",
            user = "user",
            password = "password",
            database = "database",

        )

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

        # Close Connection
        conn.close()
    
Postges_db_App().run()