from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 
from kivymd.app import MDApp 
# from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file("my_tabs2.kv")

class MyLayout(Widget):
   pass

class TabbingApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        return MyLayout()
    
if __name__ == "__main__":
    TabbingApp().run()