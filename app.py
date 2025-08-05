import requests
import json
from flask import Flask, render_template, request, jsonify
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///tickets.db")


@app.route("/", methods=["GET", "POST"])
def home():
    
    return render_template("index.html")
@app.route("/comprar" )
def comprar():
    valor = None
    # Busca todos os tickets ordenados por id
    tickets = db.execute("SELECT * FROM tickets ORDER BY id")

    for ticket in tickets:
        if ticket["use"] == "no":
            valor =ticket["valor"]
            db.execute("UPDATE tickets SET use = ? WHERE id = ?","yes", ticket["id"])
    if valor is None:
        return render_template("Nope.html") 
    

            
    return render_template("comprar.html",valor =valor )
@app.route("/info" )
def info():

    return render_template("info.html")

@app.route("/contatos", methods=["GET", "POST"])
def contatos():
    return render_template("contatos.html")


if __name__ == "__main__":
    app.run(debug=True)
