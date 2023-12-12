import os
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp

Window.size = (310,580)

Builder.load_file('cal.kv')

class MyCalculator(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    # Create a button pressing function
    def button_press(self, button):
        # Create a variable that contains whatever is in the textbox already
        prior = self.ids.calc_input.text
        # Test for Error
        if "Error" in prior:
            prior = ""
        # determine if 0 is sitting in textbox
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # Create an addition function
    def math_sign(self, sign):
        # Create a variable that contains whatever is in the textbox already
        prior = self.ids.calc_input.text
        # Put a plus sign to the textbox
        self.ids.calc_input.text = f'{prior}{sign}'
        return sign

    # Create a function to remove the last character
    def remove(self):
        # Create a variable that contains whatever is in the textbox already
        prior = self.ids.calc_input.text
        # Remove the last item in the textbox
        prior = prior[:-1]
        # Print to Textbox
        self.ids.calc_input.text = prior
        # Test for ""
        if prior == "":
            prior = "0"
        self.ids.calc_input.text = prior

    # Create function to make positive or negative signs
    def pos_neg(self):
        # Create a variable that contains whatever is in the textbox already
        prior = self.ids.calc_input.text
        # test to see if there is a - sign already
        front = prior[0]
        if front == "-":
            self.ids.calc_input.text = f'{prior.replace(front,"")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # Create a decimal function
    def dot(self):
        # Create a variable that contains whatever is in the textbox already
        prior = self.ids.calc_input.text
        # Split String
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            # Add a decimal to the end
            prior = f'{prior}.'
            # Output back to textbox
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            # Put a decimal sign to the textbox
            self.ids.calc_input.text = f'{prior}.'

    # Create Percent to Decimal function
    def percent_decimal(self):
        # Create a variable that contains whatever is in the textbox already
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        dec = int(prior) / 100
        self.ids.calc_input.text = str(dec)

    # Create the equals function
    def equals(self):
        # Create a variable that contains whatever is in the textbox already
        prior = self.ids.calc_input.text
        # Error Handling
        try:
            # Evaluate the math
            answer = eval(prior)
            # Output in textbox
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = f"Error"


class CalculatorApp(MDApp):
    def build(self):
        return MyCalculator()
    
if __name__ == '__main__':
    CalculatorApp().run()