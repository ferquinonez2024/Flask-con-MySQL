from flask import Flask
from Conexión.conexion import get_db_connection

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola Flask + MySQL!"

@app.route("/test_db")
def test_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return f"Conexión exitosa a la base de datos: {result[0]}"

if __name__ == "__main__":
    app.run(debug=True)
