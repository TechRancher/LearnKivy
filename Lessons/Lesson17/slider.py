from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp 

Builder.load_file("slider.kv")

class MyLayout(Widget):
    # Create slide_it function
    def slide_it(self, *args):
        # Set the text to the value of the slider
        self.slide_text.text = str(int(args[1]))
        # Set the text size to the value of the slider * 2
        self.slide_text.font_size = str(int(args[1]) * 2)

class TheSliderApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return MyLayout()
    
if __name__ == "__main__":
    TheSliderApp().run()