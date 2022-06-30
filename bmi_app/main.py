from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
import math

class HomeScreen(Screen):

    peso = NumericProperty(40)

    def getValue(self):
        slidervalue = self.ids.height_value
        print(slidervalue.value)
    
    def increase(self):
        self.weight = self.weight + 1 

    def decrease(self):
        self.weight = self.weight - 1 
    
    def calcular_imc(self):
        height = round(self.ids.height_value.value)/100
        height_squared = height * height
        imc = self.weight * height_squared
        print(imc)


class ResultScreen:
    pass

class MainApp (MDApp):
    def __init__(self):
        Window.size = (400,600)
        super().__init__()

MainApp().run()
