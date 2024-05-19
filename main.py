from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
import json

player = {
    "score": 0,
    "power": 1,
}
def read_data():
    global player
    try:
        with open("play.json", "r", encoding="utf-8") as file:
            player = json.load(file)
    except:
        print("1488")
def save_data():
    global player
    try:
        with open("play.json", "w", encoding="utf-8") as file:
            json.dump(player, file, indent=4, ensure_ascii=True)
    except:
        print("1488")
class Mainscreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self, *args):
        read_data()
        self.ids.score_babeltrahen.text = str(player["score"])

    def click(self):
        self.ids.pic.size_hint = (0.7, 0.8)
        self.ids.but.size_hint = (0.7, 0.8)
        read_data()
        player["score"] += player["power"]
        self.ids.score_babeltrahen.text = str(player["score"])
        save_data()

    def release(self):
        self.ids.pic.size_hint = (0.4, 0.6)
        self.ids.but.size_hint = (0.4, 0.6)


class Menuscreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def clickend(self):
        self.manager.current = "clicker"

class Clickerapp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menuscreen(name='only'))
        sm.add_widget(Mainscreen(name='clicker'))
        return sm

app = Clickerapp()
app.run()