from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    # خد القيم من الفورم
    features = [
        float(request.form['age']),
        float(request.form['gender']),
        float(request.form['neighbourhood']),
        float(request.form['scholarship']),
        float(request.form['hipertension']),
        float(request.form['diabetes']),
        float(request.form['alcoholism']),
        float(request.form['handcap']),
        float(request.form['sms']),
        float(request.form['waitingdays']),
        float(request.form['weekday']),
        float(request.form['agegroup'])
    ]

    final_features = np.array([features])
    final_features = scaler.transform(final_features)

    prediction = model.predict(final_features)

    if prediction[0] == 1:
        result = "Patient will NOT show ❌"
    else:
        result = "Patient will show ✅"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)