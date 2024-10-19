import sys
import os
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from flask_frozen import Freezer

# Configure application
app = Flask(__name__)
freezer = Freezer(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Don't update automatically each refresh
app.config['SESSION_REFRESH_EACH_REQUEST'] = False

# Don't store in cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

Session(app)

# baseUri se redefine para satisfacer a github-pages. Quizas en el host final hay que cambiarlo
# HOME PAGE
@app.route("/")
def home():
    baseUri = ""
    return render_template ("index.html", baseUri=baseUri)

# LO QUE NOS IMPORTA
@app.route("/sobre-mes-millor/")
def sobreMesMillor():
    baseUri = "."
    return render_template ("sobre-mes-millor.html", baseUri=baseUri)

# PSICONUTRICION
@app.route("/psiconutricion/")
def psiconutricion():
    baseUri = "."
    return render_template("psiconutricion.html", baseUri=baseUri)

# Clases de Yoga
@app.route("/clases-de-yoga/")
def clasesYoga():
    baseUri = "."
    return render_template("clases-de-yoga.html", baseUri=baseUri)

# Yoga para embarazadas
@app.route("/yoga-para-embarazadas/")
def yogaEmbarazadas():
    baseUri = "."
    return render_template("yoga-para-embarazadas.html", baseUri=baseUri)

# Yoga postnatal
@app.route("/yoga-postnatal/")
def yogaPostnatal():
    baseUri = "."
    return render_template("yoga-postnatal.html", baseUri=baseUri)


# 404 NOT FOUND Entrena tu mente cuida tu cuerpo
""" @app.route("/entrena-tu-mente-cuida-tu-cuerpo")
def entrenaMenteCuidaCuerpo():
    baseUri = "."
    return render_template ("entrena-tu-mente-cuida-tu-cuerpo.html", baseUri=baseUri)

# Contacto
@app.route("/contacto/")
def contacto():
    baseUri = "."
    return render_template("contacto.html", baseUri=baseUri)

# PSICOLOGIA
@app.route("/psicologia")
def psicologia():
    return render_template("psicologia-cat.html") """



if __name__ == '__main__':
    # Esta condición es importante para asegurarse de que la aplicación se ejecute
    # correctamente tanto cuando se ejecuta como una aplicación Flask en vivo
    # como cuando se genera estáticamente con Frozen-Flask.
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(debug=True)