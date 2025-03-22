from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class LikeApp(App):
    def build(self):

        self.mainBox=BoxLayout(orientation="vertical")
        btnBox=BoxLayout()
        lbl_title=Label(text="Як тобі цей кіт??????", font_size=32, halign="center", size_hint=[1,0.1])

        btn_like=Button(text="Like", font_size=24, size_hint=[0.5,0.5], on_press=self.like)
        btn_dislike=Button(text="Dislike", font_size=24, size_hint=[0.5,0.5], on_press=self.dislike)

        self.img=Image(source="photo/cat2.jpg", size_hint=[1,0.6])
        self.mainBox.add_widget(lbl_title)
        self.mainBox.add_widget(self.img)

        btnBox.add_widget(btn_like)
        btnBox.add_widget(btn_dislike)

        self.mainBox.add_widget(btnBox)
        return self.mainBox
    def like(self,btn):
        print("liked")
    def dislike(self,btn):
        print("disliked")

LikeApp().run()

