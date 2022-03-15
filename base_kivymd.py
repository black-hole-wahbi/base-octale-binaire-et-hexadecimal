from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.core.clipboard import Clipboard
screen_helper="""
Screen:
    MDLabel:
        id : txt
        text:"resulta :)"
        pos_hint:{'center_x':0.4,'center_y':0.8}
        size_hint_x:None
    MDRectangleFlatButton:
        text:"copy"
        pos_hint:{'center_x':0.8,'center_y':0.8}
        size_hint_x:None
        on_release: app.copy()
    MDTextField:
        id: nbr
        hint_text: "donne entier n"
        helper_text: "n de base decimal"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.6}
        size_hint_x:None
        width:200
    MDTextField:
        id: base
        hint_text: "donne le base "
        helper_text: "base 2 , 8 et 16"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        pos_hint:{'center_x': 0.5, 'center_y': 0.4}
        size_hint_x:None
        width:100
    MDRectangleFlatButton:
        id: btn
        text: 'conert'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            app.press()

"""
class Main(Screen):
    pass
class DemoApp(MDApp):    
    def build(self):
        return Builder.load_string(screen_helper)
    def base(self,n,b):
        ch=str()
        while n!=0:
            if n%b<=9 :
                ch=chr(n%b+48)+ch
            else:
                ch=chr(n%b+55)+ch
            n=n//b
        return ch
    def press(self,*args):
        try :
            p=self.base(int(self.root.ids.nbr.text),int(self.root.ids.base.text))
            self.root.ids.txt.text = p 
        except:
            print("error")
    def copy(self):
        ch=(self.root.ids.txt.text)
        self.text = Clipboard.paste()
        Clipboard.copy(ch)
DemoApp().run()
