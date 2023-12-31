from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.core.window import Window 

Builder.load_file("float_layout.kv")

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (.8,.8,.8,1)
        return MyLayout()
    
if __name__ == "__main__":
    AwesomeApp().run()