from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained crop recommendation model
with open('crop1.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/input')
def input():
    return render_template('newcrop.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        data1 = int(request.form.get('K'))  # Potassium
        data2 = int(request.form.get('N'))  # Nitrogen
        data3 = int(request.form.get('P'))  # Phosphorus
        data4 = float(request.form.get('H'))  # Humidity
        data5 = float(request.form.get('M'))  # pH Level
        data6 = float(request.form.get('R'))  # Rainfall
        data7 = float(request.form.get('T'))  # Temperature

        # Create a NumPy array for prediction
        input_data = np.array([[data1, data2, data3, data4, data5, data6, data7]])

        # Make a prediction using the trained model
        prediction = model.predict(input_data)

        # Convert prediction to string (in case it's a NumPy array)
        predicted_crop = str(prediction[0])

        return render_template('predict.html', predicted_crop=predicted_crop)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
