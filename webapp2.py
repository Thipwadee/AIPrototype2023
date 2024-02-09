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
    return "Hello World!"