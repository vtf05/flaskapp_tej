from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import sklearn

app = Flask(__name__,template_folder='templates')

model=pickle.load(open('model.pkl1','rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['GET','POST'])
def predict():
    int_features = []
    for x in request.form.values() :
        if  x :
            int_features.append(int(x))
        else :
            int_features.append(0)    
    final=[np.array(int_features)]
    prediction=model.predict(final)
    output=round(prediction[0], 2)

    return render_template('index.html',prediction_text='Your predicted percentage in 6th sem is.\nProbabily {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)