from crypt import methods
from doctest import debug
from flask import Flask, flash,request, redirect, render_template, make_response

import json
import sys

app = Flask(__name__)

##api
@app.route('/request',methods=['POST'])
def web_service_API():

    payload = request.data.decode("utf-8")
    imessage = json.loads(payload)

    print(imessage)
    json_data = json.dumps({'y':'received'})
    return json_data

@app.route("/")
def helloworld():
    return "<h1>Hello! Welcome to My Web Application.</h1>"

@app.route("/home", methods=['POST','GET'])
def homefn():
    if request.method == "GET":
       print('we aer in home(GET)', file=sys.stdout)

       namein = request.args.get('fname')
       print(namein, file=sys.stdout)
       return render_template("home.html", name=namein)

    elif request.method == "POST":
       print('we aer in home(POST)', file=sys.stdout)
       namein = request.form.get('fname')
       lastnamein = request.form.get('lname')
       print(namein, file=sys.stdout)
       print(lastnamein, file=sys.stdout)
       return render_template("home.html", name=namein)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5001) #host='0.0.0.0'คือสามารถให้เครื่องอื่นเห็นได้