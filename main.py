from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def search_image(self):
        # get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        # get wikipedia page and the first image link
        page = wikipedia.page(query)
        print(len(page.images))
        image_link = page.images[0]
        print(image_link)
        # download the image
        req = requests.get(image_link)
        # print(type(req))
        print(req)
        filepath = 'files/image.jpg'
        with open(filepath, 'wb') as file:
            file.write(req.content)

        # set the image in the image widget
        self.manager.current_screen.ids.img.source = filepath

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()