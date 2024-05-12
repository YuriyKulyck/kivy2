from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager

class Mainscreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def click(self):
        self.ids.pic.size_hint = (0.7, 0.8)
        self.ids.but.size_hint = (0.7, 0.8)

    def release(self):
        self.ids.pic.size_hint = (0.4, 0.6)
        self.ids.but.size_hint = (0.4, 0.6)

class Clickerapp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Mainscreen(name='only'))
        return sm

app = Clickerapp()
app.run()