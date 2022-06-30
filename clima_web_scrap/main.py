from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen

class HomeScreen():
    pass

class MainApp(MDApp):

    def __init__(self,**kwargs):
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Dark"
        Window.size = (400,600)
        super().__init__(**kwargs)

MainApp().run()