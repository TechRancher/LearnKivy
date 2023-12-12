from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp 
from kivy.core.spelling import Spelling

Builder.load_file("spell.kv")

class MyLayout(Widget):
    def press(self):
        # Create a spelling object
        spell = Spelling()
        # Select the language
        spell.select_language("en_US")
        # Get the word from the text input
        word = self.ids.word_input.text
        # If word is blank, display error
        if word == "":
            self.ids.word_label.text = "Please enter a word!"
        else:
            # Give Spelling options
            options = spell.suggest(word)
            # Loop through the options
            x = ""
            for option in options:
                x = f'{x} {option}'
            # Display the options
            self.ids.word_label.text = f'Options: {x}'
            # Clear the text input
            self.ids.word_input.text = ""
        
        
        # Check the spelling of the word
        # if spell.check(word):
        #     self.ids.word_label.text = f"{word} is a correct word!"
        # else:
        #     self.ids.word_label.text = f"{word} is a incorrect word!"

class AwesomeApp(MDApp):
    def build(self):
        Window.clearcolor = (.2,.2,.2,1)
        return MyLayout()
    
if __name__ == "__main__":
    AwesomeApp().run()