from crypt import methods
from doctest import debug
from flask import Flask, flash,request, redirect, render_template, make_response
import pickle
import json
import sys
from joblib import dump, load
import sklearn

app = Flask(__name__)
#with (open('AIPrototype2023/model (1).pk', 'rb') ) as f :
#      model = load(f)
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
        #get form data
        gender = request.form.get('gender')
        age = request.form.get('agein')
        weight = request.form.get('weightin')
        height = request.form.get('heightin')
        bmi = request.form.get('bmiin')
        temp= request.form.get('tempin')
        rh = request.form.get('rhin')
        v = request.form.get('vin')
        tmrt = request.form.get('tmrtin')
        area = request.form.get('area')
        print(gender,file=sys.stdout)
        print(age,file=sys.stdout)
        print(area,file=sys.stdout)
        #result = model.predict([[gender, age, weight, height, bmi, temp,rh,v,tmrt,area]])[0]
        return render_template('result.html') #,gender=gender, age=age, weight=weight, height=height, bmi=bmi, temp=temp,rh=rh,v=v,tmrt=tmrt,area=area)
        
    #prediction = preprocessDataAndPredict(gender, age, weight, height, bmi, temp,rh,v,tmrt,area)

    #return render_template('result.html', prediction = prediction)
    #if request.method == "GET":
    #   print('here(GET)', file=sys.stdout)
 #   model = pickle.load(open('model (1).pk','rb'))
    #   Agein = request.args.get('ticketNum')
    #   print(Agein, file=sys.stdout)
    #   return render_template("pred.html")
      
    #elif request.method == "POST":
    #   print('here (POST)', file=sys.stdout)
    #   Age = request.form.get('agein')
    #   weight = request.form.get('weightin')
    #   print(Age)
    #   print(weight)
    #   return render_template("result.html")

#def preprocessDataAndPredict(gender, age, weight, height, bmi, temp,rh,v,tmrt,area):
#    #put all inputs in array
#    test_data = [[gender, age, weight, height, bmi, temp,rh,v,tmrt,area]]
#    print(test_data)
#    #convert value data into numpy array
#    test_data = np.array(test_data)
#    #creating a dataframe
#    test_data = pd.DataFrame(test_data)
#    print(test_data)
#    #open file
#    file = open("model.pk","rb")
#    #load trained model
#    trained_model = joblib.load(file)
#    #predict
#    prediction = trained_model.predict(test_data)
#    return render_template("result.html")


@app.route("/res", methods=['POST','GET'])
def res():
       return render_template("result.html")


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
        #    return redirect(request.url
        file.save('filename')
        return render_template("Webapp.html", name='upload completed')
    
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''   


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5001) #host='0.0.0.0'คือสามารถให้เครื่องอื่นเห็นได้