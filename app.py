
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from flask import Flask, request, jsonify
import pickle
from datetime import datetime

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    year = data.get('year')
    month = data.get('month')

    input_days_numeric = (pd.to_datetime(f'{year}-{month}') - datetime(2000, 1, 1)).days

    input_month_numeric = input_days_numeric / 30  

    prediction = model.predict([[input_month_numeric]])[0]

    response = {'prediction': prediction}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
