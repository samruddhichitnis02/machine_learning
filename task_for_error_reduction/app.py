import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd


app =  Flask(__name__)  #created the instance of the Flask()
objects = pickle.load(open('model.pkl', 'rb')) #Load the trained model in to model
ohe = objects['ohe']
standard = objects['standard']
model = objects['kn_2']


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():

    Time = float(request.form['Time in seconds'])
    Acceleration_F = float(request.form['Acceleration reading in G for frontal axis'])
    Acceleration_V = float(request.form['Acceleration reading in G for vertical axis'])
    Acceleration_L = float(request.form['Acceleration reading in G for lateral axis'])
    Id_of_sensor_antenna = float(request.form['Id of sensor antenna'])
    RSSI = float(request.form['RSSI'])
    phase = float(request.form['phase'])
    frequency = float(request.form['frequency'])

    values = [[Time, Acceleration_F, Acceleration_V, Acceleration_L,Id_of_sensor_antenna,RSSI,phase, frequency]]
    features = pd.DataFrame(values,columns = [0,1,2,3,4,5,6,7])
    print(features)

    features.iloc[:,[0, 5, 7]] = standard.transform(features.iloc[:,[0, 5, 7]])

    features = ohe.transform(features).toarray()

    prediction = model.predict(features)

    if prediction == 1:
        result = 'Sitting on Bed'
    elif prediction ==2:
        result = 'Sitting on Chair'
    elif prediction ==3:
        result = 'Lying on Bed'
    else:
        result = 'Ambulating'

    return render_template('result.html', prediction_text = result)



if __name__ == '__main__':
    app.run(debug = True)