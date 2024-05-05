import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.con = sqlite3.connect('data.db')
        self.cursor = self.con.cursor()
        self.create_user_table()
        self.create_signos_vitales_table()

    def create_user_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                correo_electronico TEXT,
                contraseña TEXT,
                id_unico TEXT
            )
        ''')
        self.con.commit()

    def create_user(self, nombre, correo_electronico, contraseña, id_unico):
        self.cursor.execute('''
            INSERT INTO usuarios(nombre, correo_electronico, contraseña, id_unico) 
            VALUES(?, ?, ?, ?)
        ''', (nombre, correo_electronico, contraseña, id_unico))
        self.con.commit()

    def get_user(self, id_unico):
        user = self.cursor.execute(
            "SELECT * FROM usuarios WHERE id_unico=?", (id_unico,)).fetchone()

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

    def insert_signos_vitales(self, usuario_id, frecuencia_cardiaca, nivel_oxigeno, temperatura, datos_acelerometro, datos_giroscopio):
        self.cursor.execute('''
            INSERT INTO signos_vitales(usuario_id, frecuencia_cardiaca, nivel_oxigeno, temperatura, datos_acelerometro, datos_giroscopio) 
            VALUES(?, ?, ?, ?, ?, ?)
        ''', (usuario_id, frecuencia_cardiaca, nivel_oxigeno, temperatura, datos_acelerometro, datos_giroscopio))
        self.con.commit()

    def log_out_user(self, username):
        self.cursor.execute(
            "UPDATE usuario SET logged_in = 0 WHERE usuario = ?", (username,))
        self.con.commit()
