from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField

app = Flask(__name__)
app.config["SECRET_KEY"] = "clavesecreta"

@app.route("/")

def index():
  return render_template("index.html")


