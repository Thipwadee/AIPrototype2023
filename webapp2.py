from crypt import methods
from doctest import debug
from flask import Flask, flash,request, redirect, render_template, make_response
import pickle
import json
import sys
import numpy as np
import pandas as pd
from joblib import dump, load
import sklearn
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
with (open('../AIPrototype2023/model1.pkl', 'rb') ) as f :
      model1= load(f)
with (open('../AIPrototype2023/model2.pkl', 'rb') ) as f :
      model2= load(f)
  
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
    return "<h1> Welcome to My Web Application.</h1>"

@app.route("/home", methods=['POST','GET'])
def homefn():
       return render_template("Webapp.html")

@app.route("/form", methods=['POST','GET'])
def form_info():
    if request.method == "GET":
    #   print('here(GET)', file=sys.stdout)
        return render_template("pred.html")
    
    elif request.method == "POST":
        gender = int(request.form.get('genderin'))
        age = int(request.form.get('agein'))
        weight = int(request.form.get('weightin'))
        height = int(request.form.get('heightin'))
        #bmi = request.form.get('bmiin')
        temp= float(request.form.get('tempin'))
        rh = float(request.form.get('rhin'))
        v = float(request.form.get('vin'))
        tmrt = float(request.form.get('tmrtin'))
        area = int(request.form.get('areain'))
        seasons = int(request.form.get('seasonsin'))
        print(gender,file=sys.stdout)
        print(age,file=sys.stdout)
        print(weight,file=sys.stdout)
        print(height,file=sys.stdout)
        #print(bmi,file=sys.stdout)
        print(temp,file=sys.stdout)
        print(rh,file=sys.stdout)
        print(v,file=sys.stdout)
        print(tmrt,file=sys.stdout)
        print(area,file=sys.stdout)
        print(seasons,file=sys.stdout)

        data = [[gender, age, weight, height, temp,rh,v,tmrt,area, seasons]]

        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
    
        
        prediction = model1.predict(data_scaled)
        
        if prediction[-1] == 0:
            result_template = 'result.html'

        if prediction[-1] == 1:
            result_template = 'unaccept.html'

        return render_template(result_template,   prediction= prediction)
        #try:
        #    predictions = preprocessDataAndPredicttsv(gender, age, weight, height, temp,rh,v,tmrt,area, seasons) 
        #    prediction = preprocessDataAndPredict(gender, age, weight, height, temp,rh,v,tmrt,area, seasons)    
        #    if (prediction[0] ==0)  :
        #       result_template = 'result.html'
        #    elif (prediction[0]==1) :
        #       result_template = 'unaccept.html'

        #    return render_template(result_template, prediction=prediction, predictions=predictions)
            
    #pass prediction to template
        #except ValueError:
        #    return "Please Enter valid values"
    #    data2 = [[gender, age, weight, height, temp,rh,v,tmrt,area, seasons]]
    #    scaler = StandardScaler()
    #    data2_scaled = scaler.fit_transform(data2)
    
        
    #    predictions = model2.predict(data2_scaled)

        
#def preprocessDataAndPredict(gender, age, weight, height, temp,rh,v,tmrt,area, seasons):
    #test_data = [[gender, age, weight, height, temp,rh,v,tmrt,area, seasons]]
    #print(test_data)
    #convert value data into numpy array
    #test_data = np.array(test_data)
    #creating a dataframe
    #test_data = pd.DataFrame(test_data)
    # สร้าง DataFrame จากข้อมูลที่รับเข้ามา
#    test_data = pd.DataFrame({
#        'gender': [gender],
#        'age': [age],
#        'weight': [weight],
#        'height': [height],
#        'temp': [temp],
#        'rh': [rh],
#        'v': [v],
#        'tmrt': [tmrt],
#        'area': [area],
#        'seasons': [seasons]
#    })
#    print(test_data)

    #scaling data

    
   
    #return prediction

#def preprocessDataAndPredicttsv(gender, age, weight, height, temp,rh,v,tmrt,area, seasons):
    #put all inputs in array
    #test_data2 = [[gender, age, weight, height, temp,rh,v,tmrt,area, seasons]]
    #print(test_data2)
    #convert value data into numpy array
    #test_data2 = np.array(test_data2)
    #creating a dataframe
    #test_data2 = pd.DataFrame(test_data2)
    #print(test_data2)
    #test_data2 = pd.DataFrame({
    #    'gender': [gender],
    #    'age': [age],
    #    'weight': [weight],
    #    'height': [height],
    #    'temp': [temp],
    #    'rh': [rh],
    #    'v': [v],
    #    'tmrt': [tmrt],
    #    'area': [area],
    #    'seasons': [seasons]})
    
    #print(test_data2)
    #scaling data
    #scaler = StandardScaler()
    #test_data_scaled2 = scaler.fit_transform(test_data2)
        
    #predictions = model2.predict(test_data_scaled2)
   
    #return predictions


@app.route("/res", methods=['POST','GET'])
def res():
       return render_template("result.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5001) #host='0.0.0.0'คือสามารถให้เครื่องอื่นเห็นได้