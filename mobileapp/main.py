#from img import download_save_images
from database import Database
from kivy.core.window import Window
from kivy.utils import platform
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget
from kivymd.uix.anchorlayout import MDAnchorLayout

# ---
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton
from kivymd.uix.widget import MDWidget
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.imagelist.imagelist import MDSmartTile
# ---

from kivymd.uix.screenmanager import MDScreenManager
from kivymd.app import MDApp
import os
import sys
from datetime import datetime


if hasattr(sys, '_MEIPASS'):
    os.environ['KIVY_NO_CONSOLELOG'] = '1'

database = Database()


def validate_empty(*args):
    errors = False

    for campo in args:
        if campo.text == "":
            campo.error = True
            errors = True

    return errors


# Clase para la pantalla de inicio de sesión
class LoginScreen(MDScreen):
    def login(self):
        username = self.ids.user
        password = self.ids.password

        empty = validate_empty(username, password)

        if empty:
            self.ids.messages.text = "Todos los campos son requeridos"
            return

        res = database.get_user(username.text)

        if (res['status'] == False):
            app_instance = MDApp.get_running_app()
            self.ids.messages.text = "Usuario invalido o no registrado"
        else:
            if (res['data'][2] != password.text):
                self.ids.messages.text = "Contraseña incorrecta"
                password.error = True
                return

            self.manager.transition.direction = 'left'
            self.manager.current = 'app_screen'

    def show_new_account_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'new_account_screen'


# Clase para la pantalla de creación de nueva cuenta
class NewAccountScreen(MDScreen):

    def new_account(self): # Método para crear una nueva cuenta de usuario
        new_username = self.ids.new_user
        new_password = self.ids.new_user_password

        empty = validate_empty(new_username, new_password)

        if empty:
            self.ids.messages.text = "Todos los campos son requeridos"
            Clock.schedule_once(lambda dt: self.clean(), 2)
            return

        res = database.get_user(new_username.text)

        if (res['status'] == True):
            self.ids.messages.text = "Ya existe una cuenta con este nombre de usuario"
            Clock.schedule_once(lambda dt: self.clean(), 2)
            return

        database.create_user(new_username.text, new_password.text) 

        self.ids.messages.theme_text_color = "Custom"
        self.ids.messages.text_color = "green"
        self.ids.messages.text = "Cuenta creada con exito"

        Clock.schedule_once(lambda dt: (self.show_login_screen(), self.clean()), 2)

    def show_login_screen(self): # Método para mostrar la pantalla de inicio de sesión
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

    def clean(self): # Método para limpiar los campos de entrada
        self.ids.new_user.text = ""
        self.ids.new_user_password.text = ""
        self.ids.messages.text = ""

# Clase para la pantalla principal de la aplicación
class AppScreen(MDScreen):

    def log_out(self): # Método para cerrar sesión
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def show_history_screen(self): # Método para cerrar sesión
        self.manager.transition.direction = 'right'
        self.manager.current = "history_screen"

class HistoryScreen(MDScreen):
    pass

class MainApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        self.title = "Sistema de monitoreo de salud"

        if platform != 'android':
            #Window.size = (450, 1000) #2.2
            #Window.size = (540, 1200) #Mitad escala
            #Window.size = (414, 600) #736
            Window.size = (360, 700)
            

        self.manager = MDScreenManager()
        self.manager.add_widget(LoginScreen(name='login_screen'))
        self.manager.add_widget(AppScreen(name='app_screen'))
        self.manager.add_widget(NewAccountScreen(name='new_account_screen'))
        self.manager.add_widget(HistoryScreen(name='history_screen'))

        self.manager.current = "app_screen"

        return self.manager

    def show_new_account_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'new_account_screen'
        #self.dialog.dismiss()

    def show_new_account_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'history_screen'

    def get_screen_instance(self, screen):
        return self.root.get_screen(screen)

MainApp().run()

#pybluez para recibir datos desde esp32
#matplotlib para hacer graficos
#sqlite3 para la db local
#request para para enviar los datos a un API REST en el sw
#en el sw utilizar lara para crear una API REST que reciba los datos y los almacene en una base de datos MySQL. 
#luego utilizar lara blade para crear la página web que muestre estos datos.
