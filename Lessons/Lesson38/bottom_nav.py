from kivymd.app import MDApp
from kivy.lang import Builder 

class Bottom_Nav_App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        
        return Builder.load_file("bottom_nav.kv")
    
Bottom_Nav_App().run()