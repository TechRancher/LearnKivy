from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp 

Builder.load_file("radio.kv")

class MyLayout(Widget):
    # Create a list to hold the toppings
    checks = []
    # Create a checkbox function
    def checkbox_click(self, instance, value, Topping):
        # Check if the checkbox is checked
        if value is True:
            # Update the label
            self.ids.output_label.text = f"Your Selection: {Topping}"
        else:
            # Remove the topping from the list
            self.ids.output_label.text = f"Your Selection: {Topping}"
            # If there is no toppings selected, clear the label
            if value == False:
                self.ids.output_label.text = ""

class TheRadioApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return MyLayout()
    
if __name__ == "__main__":
    TheRadioApp().run()