from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window



class Regertelas(ScreenManager):
    pass

class Inicial(Screen):
    pass
    Window.size = (450, 650)

class Mapa(Screen):
    pass

class Sobre(Screen):
    pass

class Sadac(App):
    def build(self):
        return  Regertelas()

Sadac().run()


