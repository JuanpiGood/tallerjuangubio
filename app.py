from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hola, soy JuanGubio 🚀</h1>
    <p>Mi app Flask está funcionando correctamente.</p>
    <img src="https://via.placeholder.com/300x200?text=JuanGubio" alt="Imagen de JuanGubio">
    """

def main():
    # Render asigna dinámicamente el puerto
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()
