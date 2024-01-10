from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp 

Builder.load_file("checkBox.kv")

class MyLayout(Widget):
    # Create a list to hold the toppings
    checks = []
    # Create a checkbox function
    def checkbox_click(self, instance, value, Topping):
        # Check if the checkbox is checked
        if value is True:
            # Append the topping to the list
            self.checks.append(Topping)
            # Create a string to hold the toppings
            tops = ''
            # Loop through the list of toppings and add them to the string
            for check in MyLayout.checks:
                tops = f"{tops} {check},"
            # Update the label
            self.ids.output_label.text = f"Your Selection: {tops}"
        else:
            # Remove the topping from the list
            MyLayout.checks.remove(Topping)
            # Create a string to hold the toppings
            tops = ''
            # Loop through the list of toppings and add them to the string
            for check in MyLayout.checks:
                tops = f"{tops} {check},"
            # Update the label
            self.ids.output_label.text = f"Your Selection: {tops}"
            # If there is no toppings selected, clear the label
            if tops == '':
                self.ids.output_label.text = ""

class TheCheckBoxApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return MyLayout()
    
if __name__ == "__main__":
    TheCheckBoxApp().run()