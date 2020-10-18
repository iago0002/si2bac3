import os
from flask import Flask, jsonify, request

fibo = Flask(__name__)

@app.route('/')
def fibonacci():
   a = 1
   b = 0
   resultado = "0,"
   for i in range(51):
       tmp = a
       a += b
       b = tmp
       resultado += str(a) + ","


   return resultado

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    fibo.run(host='0.0.0.0', port=port)
