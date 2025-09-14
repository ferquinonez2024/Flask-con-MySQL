import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",       # tu usuario MySQL
        password="tu_password",  # tu contraseña
        database="desarrollo_web"
    )
    return connection
