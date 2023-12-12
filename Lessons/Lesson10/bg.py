import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('bg.kv')

class MyLayout(Widget):
    def clear_text(self):
        self.ids.name.text = ""

class MyInheritApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyInheritApp().run()