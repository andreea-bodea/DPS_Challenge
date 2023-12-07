
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from flask import Flask, request, jsonify

app = Flask(__name__)

df_initial = pd.read_csv('monatszahlen2307_verkehrsunfaelle_10_07_23_nosum.csv')

df = df_initial[df_initial['JAHR'] <= 2020]
df = df.reset_index(drop=True)
df = df[['MONATSZAHL', 'AUSPRAEGUNG', 'MONAT', 'WERT']]
df['MONATSZAHL'] = df['MONATSZAHL'].astype("string")
df['AUSPRAEGUNG'] = df['AUSPRAEGUNG'].astype("string")
df['MONAT'] = df['MONAT'].astype("string")
df['MONAT'] = pd.to_datetime(df['MONAT'].astype("string"), format='%Y%m', errors='coerce')
df = df.sort_values(by='MONAT')
df = df.reset_index(drop=True)

filtered_df = df[(df['MONATSZAHL'] == 'Alkoholunfälle') & (df['AUSPRAEGUNG'] == 'insgesamt')]
filtered_df['MONTH_NUMERIC'] = (filtered_df['MONAT'] - filtered_df['MONAT'].min()) / np.timedelta64(1, 'M')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    year = data.get('year')
    month = data.get('month')

    input_month_numeric = (pd.to_datetime(f'{year}-{month:02d}') - df['YearMonth'].min()) / np.timedelta64(1, 'M')

    X_train, X_test, y_train, y_test = train_test_split(
    filtered_df[['MONTH_NUMERIC']],
    filtered_df['WERT'],
    test_size = 0.2,  
    random_state = 42  # seed for reproducibility
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    prediction = model.predict([[input_month_numeric]])[0]

    response = {'prediction': prediction}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
