from flask import Flask, render_template, request
import pickle
import pandas as pd

obj = pickle.load(open('model.pkl','rb'))

lb = obj['lb']
ohe = obj['ohe']
classifier = obj['classifier']


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods = ['POST'])
def predict():
    try:
        amino_acid = request.form['Amino_Acid']

        X = amino_acid

        def split(word):
            return [char for char in word]

        new_data = pd.DataFrame([split(i) for i in X])
        print(new_data)


        label_encoding = lb.transform(new_data)
        print(label_encoding)


        one_hot_encoding = ohe.transform([label_encoding]).toarray()
        print(one_hot_encoding)
        print(one_hot_encoding.shape)

        prediction = classifier.predict(one_hot_encoding)

        if prediction == +1:
            result = 'yes'

        else:
            result = 'no'

        return render_template('result.html', prediction_text = result)

    except:

        return "Enter Amino Acids with 8 Letters"

if __name__ == '__main__':
    app.run(debug = True)