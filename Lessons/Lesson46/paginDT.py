from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
import dBInfo
from kivy.clock import Clock




class MDDate(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Create Database object
        self.db = dBInfo.Database()

        # Get Data from Database
        self.todo_query = "SELECT * FROM todo_list"
        self.db.c.execute(self.todo_query)
        self.todo_list = self.db.c.fetchall()

    def load_table(self):
        layout=MDBoxLayout(orientation='vertical')
        # Create KivyMD DataTable
        self.table = MDDataTable(
            size_hint=(0.9, 0.7),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            background_color_header=(0, 0.2, 0.2, .5),
            check=True,
            use_pagination=True,
            pagination_menu_height=dp(140),
            rows_num=5,
            pagination_menu_pos="center",
            column_data=[
                ("Title", dp(30)),
                ("Date", dp(20)),
                ("Description", dp(70)),
            ],
            row_data=[
                (f"{row[0]}", f"{row[1]}", f"{row[2]}") for row in self.todo_list
            ]
        )

        # Bind Table to screen
        self.table.bind(on_check_press=self.check_press)
        self.table.bind(on_row_press=self.row_press)

        # Close Connection
        self.db.conn.close()

        # Add DataTable to screen
        self.add_widget(self.table)

        

    # Function for Check Press
    def check_press(self, instance_table, current_row):
        print(current_row[3])

    # Function for Row Press
    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

class My_DataTableApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MDDate(name='mdDate'))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file('paginDT.kv')
    
    def on_start(self):
            data_screen = self..get_screen("mdData")
            data_screen.ids.table.add_widget(self.table)


My_DataTableApp().run()