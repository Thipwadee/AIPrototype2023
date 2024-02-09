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

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        #if 'file' not in request.files:
        #    flash('No file part')
        #    return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        #if file.filename == '':
        #    flash('No selected file')
        #    return redirect(request.url)
        file.save('filename')
        return render_template("home.html", name='upload completed')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5001) #host='0.0.0.0'คือสามารถให้เครื่องอื่นเห็นได้