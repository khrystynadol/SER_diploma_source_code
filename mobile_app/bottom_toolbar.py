from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem

Window.size = (300, 600)

# KV Language for UI Layout
screen_helper = """
BoxLayout:
    orientation: 'vertical'

    MDScreenManager:
        id: screen_manager

        HomeScreen:
        FavouriteScreen:
        NotificationScreen:
        ProfileScreen:

    MDRelativeLayout:
        size_hint_y: None
        height: dp(70)

        MDBottomNavigation:
            id: bottom_nav
            panel_color: 1, 1, 1, 1
            selected_color_background: 0, 0, 1, 0.2
            text_color_active: 0, 0, 1, 1

            MDBottomNavigationItem:
                name: 'home'
                text: 'Home'
                icon: 'home'
                on_tab_press: app.switch_screen('home')

            MDBottomNavigationItem:
                name: 'favourites'
                text: 'Favourites'
                icon: 'heart'
                on_tab_press: app.switch_screen('favourites')

            MDBottomNavigationItem:
                name: 'microphone'
                text: ''
                icon: ''
                disabled: True  # Spacer for the microphone button

            MDBottomNavigationItem:
                name: 'notifications'
                text: 'Notifications'
                icon: 'bell'
                on_tab_press: app.switch_screen('notifications')

            MDBottomNavigationItem:
                name: 'profile'
                text: 'Profile'
                icon: 'account'
                on_tab_press: app.switch_screen('profile')

        MDFloatingActionButton:
            icon: "microphone"
            size_hint: None, None
            size: dp(75), dp(75)
            elevation: 12
            pos_hint: {"center_x": 0.5, "center_y": 1.1}
            md_bg_color: 0, 0, 1, 1
            on_release: app.on_microphone_pressed()

<HomeScreen>:
    name: "home"
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "Recent Audios will be displayed here."
            halign: "center"

<FavouriteScreen>:
    name: "favourites"
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "Favourite Audios will be displayed here."
            halign: "center"

<NotificationScreen>:
    name: "notifications"
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "List of notifications will be displayed here."
            halign: "center"

<ProfileScreen>:
    name: "profile"
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "User profile information will be displayed here."
            halign: "center"
"""

class HomeScreen(MDScreen):
    pass


class FavouriteScreen(MDScreen):
    pass


class NotificationScreen(MDScreen):
    pass


class ProfileScreen(MDScreen):
    pass


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(screen_helper)

    def switch_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

    def on_microphone_pressed(self):
        print("Microphone button pressed")


if __name__ == "__main__":
    DemoApp().run()
