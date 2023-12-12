from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    id_number = ObjectProperty(None)
    job_number = ObjectProperty(None)

    def press(self):
        name = self.name.text
        ID = self.id_number.text
        Job = self.job_number.text


        if name == "" or ID == "" or Job == "":
            # Create a msg label
            global msg
            # msg = Label(text="You must enter information into the text boxes")
            # self.add_widget(msg)
        else:
            print(f"Hello {name}, Your ID # is {ID}, and the Job Number is {Job}.")
            # Print to Screen
            # msg.text=f"Hello {name}, Your ID # is {ID}, and the Job Number is {Job}."
            # Clear Text Boxes
            self.name.text = ""
            self.id_number.text=""
            self.job_number.text=""


class MyLabelApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyLabelApp().run()