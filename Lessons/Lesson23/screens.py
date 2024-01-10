from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp 

Builder.load_file("firstWindow.kv")

# Define different screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass    


# class MyLayout(Widget):
#     pass

class TheScreensApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        sm = ScreenManager()
        sm.add_widget(FirstWindow(name="first"))
        sm.add_widget(SecondWindow(name="second"))
        sm.current = 'first'

        return sm
    
if __name__ == "__main__":
    TheScreensApp().run()