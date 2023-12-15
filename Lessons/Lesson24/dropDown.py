from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp 

Builder.load_file("dropDown.kv")

class MyLayout(Widget):
    def menu(self):
        print("Menu button pressed")

class TheScreensApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        
        return MyLayout()
    
if __name__ == "__main__":
    TheScreensApp().run()