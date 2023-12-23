from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
import dBInfo
from kivy.metrics import dp


class DataTable_Pagin(MDApp):
    def build(self):
        # Create Screen
        screen = MDScreen()

        # Create Database object
        db = dBInfo.Database()

        # Get Data from Database
        todo_query = "SELECT * FROM todo_list"
        db.c.execute(todo_query)
        todo_list = db.c.fetchall()
        
        

        # Create KivyMD DataTable
        table = MDDataTable(
            size_hint = (0.9, 0.7),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            background_color_header = (0, 0.2, 0.2, .5),
            # background_color_cell="#451938",
            # background_color_selected_cell="e4514f",
            check = True,
            use_pagination = True,
            pagination_menu_height = dp(140),
            rows_num = 5,
            pagination_menu_pos = "center",
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
        
        print(current_row[3])

    # Function for Row Press
    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

        
        
    
DataTable_Pagin().run()