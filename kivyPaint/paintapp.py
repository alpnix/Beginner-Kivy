import random
import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.graphics import Ellipse,Line,Color
from kivy.core.window import Window

#pyinstaller --path C:\Users\NikAlp.23\AppData\Local\Programs\Python\Python37\Lib\site-packages --onefile -w paintapp.py
Window.clearcolor = (0,0,0,1)

class PaintWindow(Widget):
    def on_touch_down(self, touch):
        randomb1 = random.randint(0, 255)
        randomb2 = random.randint(0, 255)
        randomb3 = random.randint(0, 255)
        d = 30
        self.canvas.add(Color(rgb=(randomb2/255,randomb3/255,randomb1/255)))
        #self.canvas.add(Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d)))
        touch.ud["line"] = Line(points=(touch.x,touch.y))
        self.canvas.add(touch.ud["line"])
        pass

    def on_touch_move(self, touch):
        d = 30
        #self.canvas.add(Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d)))
        touch.ud["line"].points += (touch.x,touch.y)
        pass

    def on_touch_up(self, touch):
        d = 30
        #self.canvas.add(Ellipse(pos=(touch.x-d/2,touch.y-d/2),size=(d,d)))
        pass

class PaintApp(App):
    def build(self):

        rootWindow = Widget()
        self.painter = PaintWindow()
        quitbtn = Button(text="quit",size=(50,30))
        clearbtn = Button(text="clear",size=(50,30))
        modebtn = Button(text="mode",size=(50,30),pos=(60,0))
        quitbtn.bind(on_release=self.quit)
        clearbtn.bind(on_release=self.clear_canvas)
        modebtn.bind(on_release=self.change_mode)
        rootWindow.add_widget(modebtn)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clearbtn)
        #rootWindow.add_widget(quitbtn)

        return rootWindow

    def clear_canvas(self,obj):
        self.painter.canvas.clear()

    def change_mode(self,obj):
        if Window.clearcolor == (0,0,0,1):
            Window.clearcolor = (1,1,1,1)
        elif Window.clearcolor == (1,1,1,1):
            Window.clearcolor = (0,0,0,1)

    def quit(self,obj):
        App.get_running_app().stop()
        Window.close()
if __name__ == "__main__":
    PaintApp().run()
