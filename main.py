import pyrebase

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
    print(user.key())
    print(user.val())
    print("\n")
# print(users.val())