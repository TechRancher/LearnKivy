from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp 

Builder.load_file("splitter.kv")

class MyLayout(Widget):
   pass

class SplitterApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        
        return MyLayout()
    
if __name__ == "__main__":
    SplitterApp().run()