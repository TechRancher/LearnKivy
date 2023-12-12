from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window 

Builder.load_file('upDate_Label.kv')

class MyLayout(Widget):
    def press(self):
        # Assign variable to the text input value
        name = self.ids.name_input.text 
        # Assign the value of input to the label text
        self.ids.name_label.text = f'Hello {name}!'
        # clear the TextInput value
        self.ids.name_input.text = ""

class MyUpDateLabelApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()

if __name__ == "__main__":
    MyUpDateLabelApp().run()