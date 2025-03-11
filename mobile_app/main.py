from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Demo Application'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()], ["clock", lambda x: app.callback_2()]]
            elevation:5

        MDLabel:
            text: 'hello world'
            halign: 'center'
"""


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Builder.load_string(screen_helper)

        return screen

    def navigation_draw(self):
        print("Navigation")


if __name__ == "__main__":
    DemoApp().run()

# from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel
# from kivymd.uix.screen import Screen
# from kivy.lang import Builder
#
# # builder method
# helper = """
# Screen:
#     name:'About us'
#     BoxLayout:
#         orientation:'vertical'
#         MDToolbar:
#             title:'Demo'
#             left_action_items:[['menu',lambda x: app.navigation_draw()]]
#             right_action_items:[['logout',lambda x: app.navigation_draw()]]
#             elevation:10
#             md_bg_color: 0,0,100/255,1
#
#         MDLabel:
#             text:"hi"
#             halign:'center'
#         MDBottomAppBar:
#             MDToolbar:
#                 title:'Bottom'
#                 left_action_items:[['menu',lambda x: app.navigation_draw()]]
#                 elevation:10
#                 md_bg_color: 0,0,100/255,1
# """
#
#
# class Demo(MDApp):
#
#     def build(self):
#         screen = Builder.load_string(helper)
#         return screen
#
#     # lambda Function
#     def navigation_draw(self):
#         print("NavBar")
#
#
# if __name__ == "__main__":
#     Demo().run()

# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.button import MDFloatingActionButton
# from kivymd.uix.screen import Screen
# from kivymd.uix.toolbar import MDBottomAppBar
#
# KV = """
# Screen:
#     MDBottomAppBar:
#         MDToolbar:
#             type: "bottom"
#             mode: "center"
#             icon: "microphone"
#             on_action_button: app.on_microphone_pressed()
#             left_action_items: [["home", lambda x: app.on_home_pressed()], ["checkbox-marked-circle", lambda x: app.on_selected_pressed()]]
#             right_action_items: [["bell", lambda x: app.on_notifications_pressed()], ["account", lambda x: app.on_personal_info_pressed()]]
# """
#
#
# class MyApp(MDApp):
#     def build(self):
#         return Builder.load_string(KV)
#
#     def on_microphone_pressed(self):
#         print("Microphone pressed")
#
#     def on_home_pressed(self):
#         print("Home pressed")
#
#     def on_selected_pressed(self):
#         print("Selected item pressed")
#
#     def on_notifications_pressed(self):
#         print("Notifications pressed")
#
#     def on_personal_info_pressed(self):
#         print("Personal Info pressed")


# from kivy.lang import Builder
# from kivymd.app import MDApp
#
# KV = '''
# MDBoxLayout:
#     MDBottomAppBar:
#         MDTopAppBar:
#             title: "Title"
#             icon: "git"
#             type: "bottom"
#             left_action_items: [["menu", lambda x: x]]
#             mode: "end"
# '''
#
#
# class MyApp(MDApp):
#     def build(self):
#         return Builder.load_string(KV)
#
#
# if __name__ == "__main__":
#     MyApp().run()

# import kivy
#
# from kivy.app import App
# from kivy.uix.label import Label
#
# kivy.require('2.3.0')
#
#
# class MyApp(App):
#     def build(self):
#         return Label(text='Hello world')
#
#
# if __name__ == '__main__':
#     MyApp().run()
