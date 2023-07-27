from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hola mundo</p>"

@app.route("/personas")
def personas():
    r = requests.get("http://127.0.0.1:8000/api/personas/",
            auth=('jandry', '1234'))
    personas = json.loads(r.content)['results']
    return render_template("personas.html", personas=personas)

@app.route("/barrios")
def barrios():
    r = requests.get("http://127.0.0.1:8000/api/barrios/",
            auth=('jandry', '1234'))
    personas = json.loads(r.content)['results']
    return render_template("barrios.html", personas=personas)

@app.route("/localComidas")
def localComidas():
    r = requests.get("http://127.0.0.1:8000/api/localComidas/",
            auth=('jandry', '1234'))
    personas = json.loads(r.content)['results']
    return render_template("localComidas.html", personas=personas)

@app.route("/localRepuestos")
def localRepuestos():
    r = requests.get("http://127.0.0.1:8000/api/localRepuestos/",
            auth=('jandry', '1234'))
    personas = json.loads(r.content)['results']
    return render_template("localRepuestos.html", personas=personas)

app.run()
