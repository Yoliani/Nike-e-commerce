import random

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField

app = Flask(__name__)
app.config["SECRET_KEY"] = "clavesecreta"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<string:seccion>") 
def secciones(seccion): 
    if seccion == "hombre":
        nombre = "HOMBRES"
    elif seccion == "hombre":
        nombre = "HOMBRES"
    return render_template("secciones.html", nombre = nombre )

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        debug=True,
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(
            2000, 9000)  # Randomly select the port the machine hosts on.
    )
