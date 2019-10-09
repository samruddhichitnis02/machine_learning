import numpy as np
from flask import Flask, request, render_template
import pickle


app =  Flask(__name__)  #created the instance of the Flask()
model = pickle.load(open('model.pkl', 'rb')) #Load the trained model in to model



@app.route('/')
def home():
    return render_template('index.html')

#bounded /api with the method predict()
@app.route('/predict',methods=['POST'])
def predict():

    age = int(request.form['Age'])
    estimated_salary = int(request.form['Salary'])

    features = [[age, estimated_salary]]
    print(features)


    prediction = model.predict(features)
    print(prediction)

    if prediction == 1:
        result = 'click the ad'
    else:
        result = 'Does not click the ad'


    return render_template('result.html', prediction_text = result)


if __name__ == '__main__':
    app.run(debug = True)