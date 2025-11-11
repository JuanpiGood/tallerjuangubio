from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hola, soy JuanGubio 🚀</h1><p>Mi app Flask está funcionando correctamente.</p>"

if __name__ == '__main__':
    # host='0.0.0.0' permite conexiones desde cualquier IP
    # debug=True muestra errores detallados
    app.run(host='0.0.0.0', port=8080, debug=True)
