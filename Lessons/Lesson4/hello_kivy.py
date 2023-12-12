import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import time



class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=120
        self.col_force_default=True
        self.col_default_width=200

        # Create a second GridLayout
        self.top_grid = GridLayout(
                                    row_force_default=True,
                                    row_default_height=40,
                                    col_force_default=True,
                                    col_default_width=200
                                )
        self.top_grid.cols = 2

        # Add Widgets
        self.top_grid.add_widget(Label(text="Name: "))
        # Add Input Box
        self.name = TextInput(multiline=False, 
                              hint_text="Enter Your Name")
        self.top_grid.add_widget(self.name)

        # Add Widgets
        self.top_grid.add_widget(Label(text="ID#: "))
        # Add Input Box
        self.ID_Number = TextInput(multiline=False, 
                                   hint_text="Enter Your ID #")
        self.top_grid.add_widget(self.ID_Number)

        # Add Widgets
        self.top_grid.add_widget(Label(text="Job #: "))
        # Add Input Box
        self.Job_Number = TextInput(multiline=False, 
                                    hint_text="Enter Your Job #")
        self.top_grid.add_widget(self.Job_Number)

        # Add the new top_grid to our app
        self.add_widget(self.top_grid)

        # Create a Submit Button
        self.submit = Button(text="Submit", 
                             font_size=32,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=200
                             )
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget (self.submit)

    def press(self, instance):
        name = self.name.text
        ID = self.ID_Number.text
        Job = self.Job_Number.text


        if name == "" or ID == "" or Job == "":
            # Create a msg label
            global msg
            msg = Label(text="You must enter information into the text boxes")
            self.add_widget(msg)
        else:
            print(f"Hello {name}, Your ID # is {ID}, and the Job Number is {Job}.")
            # Print to Screen
            msg.text=f"Hello {name}, Your ID # is {ID}, and the Job Number is {Job}."
            # Clear Text Boxes
            self.name.text = ""
            self.ID_Number.text=""
            self.Job_Number.text=""


class MyLabelApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyLabelApp().run()