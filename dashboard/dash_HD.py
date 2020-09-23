from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/binned')
def binned():
    df = pd.read_csv("heart.csv", index_col=0).drop(columns='target')
    return df.to_html()

@app.route('/dataset')
def dataset():
    df = pd.read_csv("heart.csv")
    return df.to_html()

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/plot')
def plot():
    return render_template('plot.html')



@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form
        age = float(input['age'])
        sex = float(input['sex'])
        cp = float(input['cp'])
        restbps = float(input['restbps'])
        chol = float(input['chol'])
        fbs = float(input['fbs'])
        restecg = float(input['restecg'])
        thalach = float(input['thalach'])
        exang = float(input['exang'])
        oldpeak = float(input['oldpeak'])
        slope = float(input['slope'])
        ca = float(input['ca'])
        thal = float(input['thal'])
                  
     
        pred = Model.predict_proba([[age,sex,cp,restbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        return render_template('result.html', data=input, pred=pred)


if __name__ == '__main__':
    with open('HeartDiagnose', 'rb') as model:
        Model = pickle.load(model)
    app.run(debug=True)

