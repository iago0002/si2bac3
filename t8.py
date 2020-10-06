import os
from flask import flask, jsonify, request
from math import sqrt

app = flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    primos = "Tudo vai dar certo caros alunos!"


    return primos

if __name__ == "__main__":
    port = int(os.environ.get("port", 5000))
    app.run(host='0.0.0.0', port=portimport os
from flask import flask, jsonify, request
from math import sqrt

app = flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    primos = "Tudo vai dar certo caros alunos!"


    return primos

if __name__ == "__main__":
    port = int(os.environ.get("port", 5000))
    app.run(host='0.0.0.0', port=port)
~
~
~
)
