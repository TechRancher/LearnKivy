from kivymd.app import MDApp
from kivy.lang import Builder 
import mysql.connector

class MySQL_db_App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create Database or Connect to one
        mydb = mysql.connector.connect(
            host = "host",
            user = "user",
            password = "password",
            database = "database"

        )

        # Create Cursor
        c = mydb.cursor()

        # Create Database
        c.execute("CREATE DATABASE IF NOT EXISTS second_db")

        # Check to see if Database was created
        # c.execute("SHOW DATABASES")
        # for db in c:
        #     print(db[0])

        # Create Table
        c.execute("""CREATE TABLE IF NOT EXISTS customers (
            first_name VARCHAR(75)
        )""")

        # Check to see if Table was created
        # c.execute("SELECT * FROM customers")
        # print(c.description)

        # Commit Changes
        mydb.commit()

        # Close Connection
        mydb.close()

        return Builder.load_file("mySQLDB.kv")
    

    
    def submit(self):
         # Create Database or Connect to one
        mydb = mysql.connector.connect(
            host = "host",
            user = "user",
            password = "password",
            database = "database"

        )

        # Create Cursor
        c = mydb.cursor()

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
        mydb.commit()

        # Close Connection
        mydb.close()

    def show_records(self):
          # Create Database or Connect to one
        mydb = mysql.connector.connect(
            host = "host",
            user = "user",
            password = "password",
            database = "database"

        )

        # Create Cursor
        c = mydb.cursor()

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
        mydb.close()
    
MySQL_db_App().run()