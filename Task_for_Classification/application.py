import numpy as np
from flask import Flask, request, render_template
import pickle




app =  Flask(__name__)  #created the instance of the Flask()
objects = pickle.load(open('model.pkl', 'rb')) #Load the trained model in to model
standard_x = objects['standard_x']
model = objects['model']


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():

    Time = float(request.form['Time(secs)'])
    Acceleration_G_F = float(request.form['Acceleration_G(frontal axis)'])
    Acceleration_G_V = float(request.form['Acceleratoin_g(vertical axis)'])
    Acceleration_G_L = float(request.form['Acceleration_G(lateral axis)'])
    Id_of_sensor_antenna = float(request.form['Id_of_sensor_antenna'])
    RSSI = float(request.form['RSSI'])
    phase = float(request.form['phase'])
    frequency = float(request.form['frequency'])

    features = [[Time, Acceleration_G_F, Acceleration_G_V, Acceleration_G_L,Id_of_sensor_antenna,RSSI,phase, frequency]]
    scaled_features = standard_x.transform(features)
    prediction = model.predict(scaled_features)

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