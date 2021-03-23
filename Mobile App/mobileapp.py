import random
from helpers import list_helper,screen_helper
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

Window.size = (360, 600)

class HomeScreen(Screen):
    pass

class PaintScreen(Screen):
    pass

sm = ScreenManager(id="screen_manager")
sm.id = "screen_manager"
sm.add_widget(HomeScreen(name="home"))
sm.add_widget(PaintScreen(name="paint"))

class DemoApp(MDApp):
    title = "Nixapp"

    def build(self):
        themes = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green',
                  'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'BlueGray']

        self.theme_cls.primary_palette = themes[random.randint(0, len(themes) - 1)]
        self.theme_cls.theme_style = "Light"
        self.root = Builder.load_string(screen_helper)

        return self.root

    def empty(self):
        pass


DemoApp().run()
