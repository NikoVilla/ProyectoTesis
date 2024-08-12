import sqlite3
import bcrypt
from datetime import datetime

class Database:
    def __init__(self):
        self.con = sqlite3.connect('C:\\ProyectoTesis\\mobileapp\\data.db')
        self.cursor = self.con.cursor()
        self.create_user_table()
        self.create_signos_vitales_table()

    def create_user_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT UNIQUE,
                contraseña TEXT
            )
        ''')
        self.con.commit()

    def create_user(self, nombre, contraseña):
        self.cursor.execute('''
            INSERT INTO usuarios(nombre, contraseña) 
            VALUES(?, ?)
        ''', (nombre, contraseña))
        self.con.commit()

    def get_user(self, nombre):
        user = self.cursor.execute(
            "SELECT * FROM usuarios WHERE nombre=?", (nombre,)).fetchone()

        if user:
            return {'status': True, 'data': user}
        else:
            return {'status': False}


    def create_signos_vitales_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS signos_vitales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                frecuencia_cardiaca INTEGER,
                nivel_oxigeno INTEGER,
                temperatura REAL,
                datos_acelerometro TEXT,
                datos_giroscopio TEXT,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        ''')
        self.con.commit()

    # def insert_signos_vitales(self, usuario_id, frecuencia_cardiaca, nivel_oxigeno, temperatura, datos_acelerometro, datos_giroscopio):
    #     self.cursor.execute('''
    #         INSERT INTO signos_vitales(usuario_id, frecuencia_cardiaca, nivel_oxigeno, temperatura, datos_acelerometro, datos_giroscopio) 
    #         VALUES(?, ?, ?, ?, ?, ?)
    #     ''', (usuario_id, frecuencia_cardiaca, nivel_oxigeno, temperatura, datos_acelerometro, datos_giroscopio))
    #     self.con.commit()

    def log_out_user(self, username):
        self.cursor.execute(
            "UPDATE usuario SET logged_in = 0 WHERE usuario = ?", (username,))
        self.con.commit()
