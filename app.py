from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('purchase_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    input_data = {}

    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            gender = int(request.form['gender'])  
            income = float(request.form['income'])
            purchases = int(request.form['purchases'])
            category = int(request.form['category'])
            time_spent = float(request.form['time_spent'])
            loyalty = int(request.form['loyalty'])
            discounts = int(request.form['discounts'])

            input_data = {
                'age': age, 'gender': gender, 'income': income,
                'purchases': purchases, 'category': category,
                'time_spent': time_spent, 'loyalty': loyalty,
                'discounts': discounts
            }

            features = np.array([[age, gender, income, purchases, category, time_spent, loyalty, discounts]])
            scaled = scaler.transform(features)
            pred = model.predict(scaled)
            prediction = "Customer Will Purchase ✅" if pred[0] == 1 else "Customer Will Not Purchase ❌"
        except Exception as e:
            prediction = f"Error in input: {str(e)}"

    return render_template('index.html', prediction=prediction, input_data=input_data)

if __name__ == '__main__':
    app.run(debug=True)
