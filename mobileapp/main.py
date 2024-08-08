#from img import download_save_images
from daatabase1 import Database
from kivy.core.window import Window
from kivy.utils import platform
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
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
from kivy.lang import Builder
from kivy.uix.popup import Popup
from bleak import BleakClient, discover
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.app import MDApp
from datetime import datetime
import os
import sys
import bluetooth
import serial 
import json

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

class NewAccountScreen(MDScreen):

    def new_account(self):
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

    def show_login_screen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

    def clean(self):
        self.ids.new_user.text = ""
        self.ids.new_user_password.text = ""
        self.ids.messages.text = ""

class AppScreen(MDScreen):

    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def show_history_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "history_screen"

    def show_devices_screen(self): 
        self.manager.transition.direction = 'left'
        self.manager.current = "devices_screen"

class HistoryScreen(MDScreen):

    def show_app_screen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "app_screen"
    

class BottomPanel(BoxLayout):
    def show_app_screen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "app_screen"

    def show_history_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "history_screen"

    def show_devices_screen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "devices_screen"

class TopPanel(BoxLayout):
    def show_app_screen(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "app_screen"

class DevicesScreen(MDScreen):
   pass

class SignosCard(MDCard):
    titulo_card = StringProperty("")
    valor_signo = StringProperty("")
    rango = StringProperty("")
    estado = StringProperty("")

class MainApp(MDApp):
    dialog = None
    device_list = []
    client = None
    serial_port = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        self.title = "Sistema de monitoreo de salud"

        if platform != 'android':
            Window.size = (414, 736)
            #COM5 recibe
            
        self.manager = MDScreenManager()
        self.manager.add_widget(LoginScreen(name='login_screen'))
        self.manager.add_widget(AppScreen(name='app_screen'))
        self.manager.add_widget(NewAccountScreen(name='new_account_screen'))
        self.manager.add_widget(HistoryScreen(name='history_screen'))
        self.manager.add_widget(DevicesScreen(name='devices_screen'))

        self.manager.current = "app_screen"

        return self.manager

    def show_new_account_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'new_account_screen'

    def get_screen_instance(self, screen):
        return self.root.get_screen(screen)
    
    def on_start(self):
        self.connect_serial_port()
        #self.list_paired_devices()
        #self.connect_bluetooth()

    def connect_serial_port(self):
        try:
            self.serial_port = serial.Serial('COM5', baudrate=9600, timeout=1)
            Clock.schedule_interval(self.read_sensor_data, 1)
        except serial.SerialException as e:
            print(f"Error connecting to serial port: {e}")

    def read_sensor_data(self, dt):
        try:
            if self.serial_port.in_waiting > 0:
                data = self.serial_port.readline().decode('utf-8').strip()
                if data:
                    print(f"Received: {data}")
                    sensor_data = json.loads(data)
                    sensor1 = sensor_data['randomNumber1']
                    sensor2 = sensor_data['randomNumber2']
                    sensor3 = sensor_data['randomNumber3']
                    sensor4 = sensor_data['randomNumber4']
                    self.manager.get_screen('app_screen').ids.frecuencia_cardiaca.valor_signo = str(sensor1)
                    self.manager.get_screen('app_screen').ids.saturacion_oxigeno.valor_signo = str(sensor2)
                    self.manager.get_screen('app_screen').ids.temperatura_corporal.valor_signo = str(sensor3)
                    self.manager.get_screen('app_screen').ids.velocidad_angular.valor_signo = str(sensor4)
                    self.save_data_to_file(data)
        except serial.SerialException as e:
            print(f"Error reading from serial port: {e}")

    def save_data_to_file(self, data):
        with open("sensor_data.txt", "a") as file:
            file.write(f"{data}\n")

    def show_paired_devices(self):
        devices = bluetooth.discover_devices(duration=2, lookup_names=True, flush_cache=True, lookup_class=False)
        device_list = MDList()
        for addr, name in devices:
            device_list.add_widget(
                OneLineListItem(text=f"Dispositivo: {name}, Dirección MAC: {addr}")
            )
        
        self.dialog = MDDialog(
            title="Dispositivos Emparejados",
            type="custom",
            content_cls=device_list,
            buttons=[
                MDFlatButton(
                    text="CERRAR",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )
        self.dialog.open()

#PARA PYBLUEZ

    # def connect_bluetooth(self):
    #     try:
    #         self.bt_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    #         self.bt_socket.connect(("0C:B8:15:5A:4D:76", 1))  # Usa la dirección del ESP32_CAM
    #         Clock.schedule_interval(self.read_sensor_data, 1)
    #     except bluetooth.btcommon.BluetoothError as err:
    #         print(f"Error connecting to Bluetooth device: {err}")

    # def read_sensor_data(self, dt):
    #     try:
    #         data = self.bt_socket.recv(1024).decode('utf-8')
    #         self.root.ids.sensor_label.text = f"Sensor Value: {data}"
    #         self.save_data_to_file(data)
    #     except bluetooth.btcommon.BluetoothError as err:
    #         print(f"Error reading from Bluetooth device: {err}")

    # def save_data_to_file(self, data):
    #     with open("sensor_data.txt", "a") as file:
    #         file.write(f"{data}\n")

#PARA PYBLUEZ

if __name__ == '__main__':
    app = MainApp()
    app.run()

#pybluez para recibir datos desde esp32
#matplotlib para hacer graficos
#sqlite3 para la db local
#request para para enviar los datos a un API REST en el sw
#en el sw utilizar lara para crear una API REST que reciba los datos y los almacene en una base de datos MySQL. 
#luego utilizar lara blade para crear la página web que muestre estos datos.
