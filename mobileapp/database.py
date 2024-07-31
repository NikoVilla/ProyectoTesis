import sqlite3
from datetime import datetime


class Database:
    def __init__(self):
        self.con = sqlite3.connect('data.db')
        self.cursor = self.con.cursor()
        self.create_user_table()
        self.create_books_table()

        if len(self.get_all_books()) == 0:
            self.inserts_books_by_default()

    def create_user_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS usuario(id integer PRIMARY KEY AUTOINCREMENT, usuario varchar(60) NOT NULL, password varchar(60) NOT NULL, logged_in integer NOT NULL DEFAULT 0)") 
        self.con.commit()

    def create_user(self, usuario, password):
        self.cursor.execute(
            "INSERT INTO usuario(usuario, password, logged_in) VALUES(?, ?, 0)", (usuario, password))
        self.con.commit()

    def get_user(self, username):
        user = self.cursor.execute(
            "SELECT * FROM usuario WHERE usuario=?", (username,)).fetchone()

        if user:
            return {'status': True, 'data': user}
        else:
            return {'status': False}

    def log_out_user(self, username):
        self.cursor.execute(
            "UPDATE usuario SET logged_in = 0 WHERE usuario = ?", (username,))
        self.con.commit()

    def create_books_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY AUTOINCREMENT, egd TEXT NOT NULL, spo2 TEXT NOT NULL, temp TEXT NOT NULL, giro REAL NOT NULL, estado TEXT NOT NULL, fecha TEXT NOT NULL, hora TEXT NOT NULL)")
        self.con.commit()

    def create_history_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS registros(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, autor TEXT NOT NULL, fecha TEXT NOT NULL, precio REAL NOT NULL, categoria TEXT NOT NULL, descripcion TEXT NOT NULL, idioma TEXT NOT NULL)")
        self.con.commit()

    def inserts_registros_by_default(self):
        registros = [
            {
                "titulo": "Don Quijote",
                "autor": "Miguel de Cervantes",
                "fecha": datetime(1605, 1, 1),
                "precio": 15000,
                "categoria": "Novela",
                "descripcion": "Don Quijote de la Mancha es una novela que satiriza las novelas de caballería y la sociedad de la época.",
                "idioma": "Español"
            }
        ]

        for registro in registros:
            self.cursor.execute("INSERT INTO registros (egd, spo2, temp, giro, estado, fecha, hora) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                (registro["titulo"], registro["autor"], registro["fecha"], registro["precio"], registro["categoria"], registro["descripcion"], book["idioma"]))

            self.con.commit()

    def insert_book(self, titulo, autor, fecha, precio, categoria, descripcion, idioma):

        if fecha != "":
            fecha_original = fecha
            fecha_objeto = datetime.strptime(fecha_original, "%A %d %B %Y")
            fecha = fecha_objeto.strftime("%Y-%m-%d %H:%M:%S")

        self.cursor.execute(
            "INSERT INTO libros(titulo, autor, fecha, precio, categoria, descripcion, idioma) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (titulo, autor, fecha, precio, categoria, descripcion, idioma)
        )
        self.con.commit()

        book = self.search_books(titulo)

        if book:
            return book[0]

    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM libros WHERE id=?", (book_id,))
        self.con.commit()

    def update_book(self, book_id, titulo, autor, fecha, precio, categoria, descripcion, idioma):

        if fecha != "":
            fecha_original = fecha
            fecha_objeto = datetime.strptime(fecha_original, "%A %d %B %Y")
            fecha = fecha_objeto.strftime("%Y-%m-%d %H:%M:%S")

        self.cursor.execute(
            "UPDATE libros SET titulo=?, autor=?, fecha=?, precio=?, categoria=?, descripcion=?, idioma=? WHERE id=?",
            (titulo, autor, fecha, precio, categoria,
             descripcion, idioma, book_id)
        )
        self.con.commit()

    def search_books(self, search):
        books = self.cursor.execute(
            "SELECT * FROM libros WHERE titulo LIKE ? OR autor LIKE ?",
            (f"%{search}%", f"%{search}%")
        ).fetchone()
        return books

    def get_all_books(self):
        books = self.cursor.execute("SELECT * FROM libros").fetchall()
        return books

    def get_books_by_category(self, categoria):
        books = self.cursor.execute(
            "SELECT * FROM libros WHERE categoria = ?",
            (categoria,)
        ).fetchall()
        return books

    def close_db_connection(self):
        self.con.close()