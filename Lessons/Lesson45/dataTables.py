from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
import myConnection as mc
from kivy.metrics import dp

class DataTable(MDApp):
    def build(self):
        # Create Database object
        db = mc.MyConnect()
        
        screen = Screen()

        # Create Table
        db.conn.execute("""CREATE TABLE IF NOT EXISTS todo_list (
            title VARCHAR(75), date DATE, description VARCHAR(255), done BOOLEAN
        )""");

        # Commit Changes
        db.conn.commit()

        # Get Data from Database
        todo_query = "SELECT * FROM todo_list"
        db.conn.execute(todo_query)
        todo_list = db.conn.fetchall()
        
        

        # Create KivyMD DataTable
        table = MDDataTable(
            size_hint = (0.9, 0.6),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            check=True,
            use_pagination=True,
            pagination_menu_height=dp(140),
            rows_num=5,
            pagination_menu_pos="center",
            column_data = [
                ("Title", dp(30)),
                ("Date", dp(20)),
                ("Description", dp(70)),
            ],
            row_data = [
                (f"{row[0]}", f"{row[1]}", f"{row[2]}") for row in todo_list
            ]
        )

        # Bind Table to screen
        table.bind(on_check_press = self.check_press)
        table.bind(on_row_press = self.row_press)

        # Close Connection
        db.conn.close()

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # Add DataTable to screen
        screen.add_widget(table)
        # return Builder.load_file('dataTables.kv')
        return screen

    # Function for Check Press
    def check_press(self, instance_table, current_row):
        
        print(current_row[2])

    # Function for Row Press
    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

        
        
    
DataTable().run()