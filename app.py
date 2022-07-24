import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from flask_cors import cross_origin

app=Flask(__name__)


with open('linear_regression.pkl','rb') as f1:
	model=pickle.load(f1)
	

@app.route("/")
@cross_origin()
def index():
	return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
@cross_origin()
def predict():
	if request.method=="POST":
		deep_sleep=int(request.form["deep_sleep"])
		heart_rate=int(request.form["heart_rate"])
		restlessness=float(request.form["restlessness"])
		if deep_sleep<=180 and (heart_rate>=60 and heart_rate<=120) and restlessness<=1:
			df=pd.concat([pd.Series(deep_sleep),pd.Series(heart_rate),pd.Series(restlessness)],axis=1)
			prediction=str(np.round(model.predict(df),1)).strip('[]')
		else:
			prediction='Details not valid!'
		return render_template('index.html',prediction_text=str(prediction))

	return render_template("index.html")



if __name__=="__main__":
	app.run(debug=True)
