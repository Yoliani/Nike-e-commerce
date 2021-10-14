from flask import Flask, render_template, request
from flask.helpers import  url_for

from werkzeug.utils import redirect


app = Flask(__name__)
app.config["SECRET_KEY"] = "clavesecreta"


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login/", methods=['POST', 'GET'])
def iniciodesesion():
    if request.method == 'POST':
        return render_template("iniciodesesion.html")
    else:
        return render_template("iniciodesesion.html")


@app.route('/register')
def register():
    return render_template('registro.html')


@app.route("/seccion/<string:seccion>")
def secciones(seccion):
    print(seccion)
    nombre = None
    if seccion == "hombre":
        nombre = "HOMBRES"
    elif seccion == "mujer":
        nombre = "MUJERES"
    elif seccion == "niño":
        nombre = "NIÑOS"
    elif seccion == "descuento":
        nombre = "DESCUENTOS"
    
    if nombre == None:
        return redirect(url_for('error'))
    else:
        return render_template("secciones.html", nombre=nombre)


@app.route('/carrito')
def carrito():
    return render_template("carrito.html")


@app.route("/productos/<string:seccion>")
def productos(seccion):
    return render_template("productos.html", data=seccion)


@app.route('/error')
def error():
    return render_template("error.html")


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        debug=True,
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=5000

            #random.randint(
           # 2000, 9000)  # Randomly select the port the machine hosts on.
    )
