from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.button import MDIconButton
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel

# Window.size = (400, 600)
Window.size = (300, 600)

# KV Language for UI Layout
screen_helper = """
BoxLayout:
    orientation: 'vertical'
    # md_bg_color: 0.992, 0.957, 0.863, 1
    
    MDTopAppBar:
        title: "Logo"
        anchor_title: "left"
        height: dp(20)
        left_action_items: []
        right_action_items: [["cog", lambda x: app.on_settings_pressed()]]
        elevation: 3
        md_bg_color: 0.427, 0.592, 0.451, 1
        # theme_text_color: "Custom"
        # text_color: 0.992, 0.957, 0.863, 1
    
    # MDBoxLayout:
    #     size_hint_y: None
    #     height: dp(40)
    #     padding: dp(10)
    #     spacing: dp(10)
    # 
    #     MDLabel:
    #         text: "Logo"
    #         font_style: "Subtitle2"
    #         # size_hint_x: 0.9
    #         valign: "center"
    #         halign: "left"
    #         padding: dp(10), 0, 0, 0
    # 
    #     MDIconButton:
    #         icon: "cog"
    #         user_font_size: "24sp"
    #         theme_text_color: "Primary"
    #         on_release: app.on_settings_pressed()
    #         valign: "center"
    #         halign: "right"
    #         padding: 0, dp(15), dp(10), 0

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
            selected_color_background: 0.427, 0.592, 0.451, 0.2
            text_color_active: 0.427, 0.592, 0.451, 1
            # text_color_active: 0.047, 0.231, 0.180, 1
            font_style: "Caption"

            MDBottomNavigationItem:
                name: 'home'
                text: 'Home'
                icon: 'home'
                font_style: "Caption"
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
                disabled: True

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
            # theme_icon_color: "Custom"
            # icon_color: 0.992, 0.957, 0.863, 1
            size_hint: None, None
            # size: dp(75), dp(75)
            elevation: 3
            pos_hint: {"center_x": 0.5, "center_y": 1.1}
            md_bg_color: 0.047, 0.231, 0.180, 1
            on_release: app.on_microphone_pressed()

<HomeScreen>:
    name: "home"
    
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
                
        MDSeparator:
            height: dp(1)
        
        MDBoxLayout:
            width: dp(500)
            size_hint_y: None
            orientation: 'horizontal'
            
            # MDIconButton:
            #     icon: "folder"
            #     user_font_size: "100sp" 
            #     theme_text_color: "Primary"
            #     on_release: app.on_upload_pressed()

            MDIconButton:
                icon: "folder"
                font_size: "50sp"
                # theme_text_color: "Primary"
                halign: "center"
                theme_icon_color: "Custom"
                icon_color: 0.047, 0.231, 0.180, 1
                on_release: app.on_upload_pressed()

            MDLabel:
                text: "Upload File"
                size_hint_x: 0.5
                on_ref_press: app.on_upload_pressed()
                valign: "center"
                padding: 0, 5, 0, 0
                theme_text_color: "Custom"
                text_color: 0.047, 0.231, 0.180, 1
                
        # MDBoxLayout:
        #     orientation: 'vertical'
        #     size_hint_y: None
        #     height: dp(100)
        #     spacing: dp(10)
        #     pos_hint: {"center_x": 0.5}
        # 
        #     MDIconButton:
        #         icon: "folder"
        #         user_font_size: "60sp"  # Bigger folder icon
        #         pos_hint: {"center_x": 0.5}
        #         on_release: app.on_upload_pressed()
        # 
        #     MDLabel:
        #         text: "Upload File"
        #         halign: "center"
        #         theme_text_color: "Primary"
        #         font_style: "H6"
        #         on_ref_press: app.on_upload_pressed()

        MDSeparator:
            height: dp(1)

        MDLabel:
            text: "Recent Audios will be displayed here."
            halign: "center"
            theme_text_color: "Secondary"
            font_style: "Subtitle1"
            padding: dp(10)

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
        self.theme_cls.material_style = "M3"
        return Builder.load_string(screen_helper)

    def switch_screen(self, screen_name):
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = screen_name

    def on_upload_pressed(self):
        # Open the file chooser to select an audio file
        content = FileChooserIconView()
        content.bind(on_selection=lambda *x: self.select_file(content))
        self.popup = Popup(title="Select Audio File", content=content, size_hint=(0.8, 0.8))
        self.popup.open()

    def select_file(self, filechooser):
        selected_file = filechooser.selection
        if selected_file:
            print(f"Selected file: {selected_file[0]}")
            # You can add code here to handle the audio file (e.g., uploading or playing it)
        self.popup.dismiss()


if __name__ == "__main__":
    DemoApp().run()
