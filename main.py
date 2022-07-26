from numpy import average
import pyrebase
from flask import Flask, render_template, request
from flask_cors import cross_origin
import random

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

good = ['a', 'b', 'c']
bad = ['Going to bed when you feel tired and getting up at roughly the same time helps teach your body to sleep better. Try to avoid napping where possible.', 'Dark, quiet and cool environments generally make it easier to fall asleep and stay asleep. Watch our video for tips on how to sleep better.', 'If you often lie awake worrying about tomorrow, set aside time before bed to make a list for the next day. This can help put your mind at rest.']
avg = ['g', 'h', 'i']

if(valBP >= 40 and valBP <=60 and valSpO2>=98 and valSpO2<=100 and valTemp>=96.6 and valTemp<=98.6):
    sentence = "Best sleep quality!"
elif(valBP >= 40 and valBP <=60 and valSpO2>=98 and valSpO2<=100 and not(valTemp>=96.6 and valTemp<=98.6)):
    sentence = "Good sleep quality!"
elif(valBP >= 40 and valBP <=60 and not(valSpO2>=98 and valSpO2<=100) and (valTemp>=96.6 and valTemp<=98.6)):
    sentence = "Good sleep quality!"
elif(not(valBP >= 40 and valBP <=60) and valSpO2>=98 and valSpO2<=100 and not(valTemp>=96.6 and valTemp<=98.6)):
    sentence = "Good sleep quality!"

elif(valBP >= 100 and valSpO2<=90 and (valTemp>=98.6 or valTemp<=96.6)):
    sentence = "Bad sleep quality!"
elif(not(valBP >= 100) and valSpO2<=90 and (valTemp>=98.6 or valTemp<=96.6)):
    sentence = "Bad sleep quality!"
elif(valBP >= 100 and not(valSpO2<=90) and (valTemp>=98.6 or valTemp<=96.6)):
    sentence = "Bad sleep quality!"
elif(valBP >= 100 and valSpO2<=90 and not(valTemp>=98.6 or valTemp<=96.6)):
    sentence = "Bad sleep quality!"

else:
    sentence = "Average sleep quality!"

if(sentence == "Best sleep quality!" or sentence == "Good sleep quality!"):
    random_index = random.randrange(len(good))
    recommendation = good[random_index]

if(sentence == "Bad sleep quality!"):
    random_index = random.randrange(len(bad))
    recommendation = bad[random_index]
    print(recommendation)

if(sentence == "Average sleep quality!"):
    random_index = random.randrange(len(avg))
    recommendation = avg[random_index]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/quality")
def quality():
    return render_template("quality.html", valBP=valBP, valSpO2=valSpO2, valTemp=valTemp, sentence=sentence, recommendation=recommendation)

if __name__=="__main__":
    app.run(debug=True)