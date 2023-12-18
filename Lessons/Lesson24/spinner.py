from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp 

Builder.load_file("spinner.kv")

class MyLayout(Widget):
   def spinner_clicked(self, value):
         self.ids.click_label.text = f"You selected: {value}"

class TheSpinnerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        
        return MyLayout()
    
if __name__ == "__main__":
    TheSpinnerApp().run()