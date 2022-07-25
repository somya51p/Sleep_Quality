import pyrebase
from flask import Flask, render_template, request
from flask_cors import cross_origin

app=Flask(__name__)

firebaseConfig = {
    "apiKey" : "AIzaSyAlYbgA4MNsmk2qWLS1t3xLeVYA12gUH5Y",
    "authDomain" : "sleep-tracker-cff8f.firebaseapp.com",
    "databaseURL" : "https://sleep-tracker-cff8f-default-rtdb.firebaseio.com",
    "projectId" : "sleep-tracker-cff8f",
    "storageBucket" : "sleep-tracker-cff8f.appspot.com",
    "messagingSenderId" : "65629531827",
    "appId" : "1:65629531827:web:45ba902eac24fc81340ac6",
    "measurementId" : "G-JCP0RWVZGK"
}

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

auth=firebase.database()

users = db.child("new/json").get()

for user in users.each():
    count = 0
    sum = 0
    if(user.key() == "BP"):
        for key, value in user.val().items():
            sum += value
            count = count + 1
   
        valBP = float(sum / count)

    if(user.key() == "SpO2"):
        for key, value in user.val().items():
            sum += value
            count = count + 1
   
        valSpO2 = float(sum / count)

    if(user.key() == "temperature"):
        for key, value in user.val().items():
            sum += value
            count = count + 1
   
        valTemp = float(sum / count)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/quality")
def quality():
    return render_template("quality.html", valBP=valBP, valSpO2=valSpO2, valTemp=valTemp)

if __name__=="__main__":
    app.run(debug=True)