import random

from flask import Flask, render_template
from flask.helpers import flash, url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField

app = Flask(__name__)
app.config["SECRET_KEY"] = "clavesecreta"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:seccion>")
def secciones(seccion):
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


@app.route("/productos/<string:seccion>") 
def productos(seccion): 
  return render_template("productos.html", data = seccion)

@app.route('/error')
def error():
    return render_template("error.html")


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        debug=True,
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(
            2000, 9000)  # Randomly select the port the machine hosts on.
    )
