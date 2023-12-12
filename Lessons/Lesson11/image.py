from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window 

Builder.load_file('image.kv')

class MyImageLayout(Widget):
    pass

class MyInheritApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyImageLayout()

if __name__ == "__main__":
    MyInheritApp().run()