from crypt import methods
from doctest import debug
from flask import Flask, request, render_template, make_response

import json
import sys

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/name")
def hellonuey():
    return "Hello, Nuey!"

@app.route("/home", methods=['POST','GET'])
def homefn():
    if request.methods == "GET":
       print('we aer in home(GET)', file=sys.stdout)

       namein = request.args.get('fname')
       print(namein, file=sys.stdout)
       return render_template("home.html", name=namein)

    elif request.methods == "POST":
       print('we aer in home(POST)', file=sys.stdout)
       namein = request.form.get('fname')
       lastnamein = request.form.get('lname')
       print(namein, file=sys.stdout)
       print(lastnamein, file=sys.stdout)
       return render_template("home.html", name=namein)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5001) #host='0.0.0.0'คือสามารถให้เครื่องอื่นเห็นได้