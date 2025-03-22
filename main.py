from kivy.app import App

from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class FindYourCatApp(App):
    def build(self):
        self.mainBox = BoxLayout(orientation='vertical')
        btnBox=BoxLayout()
        lbl_title = Label(text="Оцініть картинку", font_size=32, halign="center", size_hint=[1,0.1])

        btn_like = Button(text="like", font_size = 24, size_hint=[0.5, 0.3], on_press=self.like)
        btn_dislike = Button(text='dislike', font_size=24, size_hint=[0.5,0.3], on_press=self.dislike)

        self.img = Image(source="89534151-13837875-image-a-22_1726052440056.png", size_hint=[1, 0.6])

        self.mainBox.add_widget(lbl_title)
        self.mainBox.add_widget(self.img)

        btnBox.add_widget(btn_like)
        btnBox.add_widget(btn_dislike)

        self.mainBox.add_widget(btnBox)
        return self.mainBox
    
    def like(self, btn):
        print("like")
    def dislike(self, btn):
        print("dislike")
FindYourCatApp().run()
