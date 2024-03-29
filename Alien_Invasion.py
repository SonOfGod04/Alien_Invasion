import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

# Create flask app
app = Flask(__name__)

# Load the stacked model
stacked_model = joblib.load(r'C:\Users\ADMIN\stacking_model.pkl')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    n_features = [float(x) for x in request.form.values()]
    features = [np.array(n_features)]
    
    # Correct the model name from 'stacking_model' to 'stacked_model'
    prediction = stacked_model.predict(features)
    
    print('prediction value is', prediction[0])
    
    if prediction[0] == 1:
        output = "No use"
    elif prediction[0] == 0:
        output = "Long_time"
    else:
        output = "short_time"
    
    return render_template("index.html", prediction_text="The Contraception used is {}".format(output))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    
    # Correct the model name from 'stacking_model' to 'stacked_model'
    prediction = stacked_model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=False)
