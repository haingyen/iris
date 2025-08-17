from flask import Flask, request, jsonify
# import joblib
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model (global scope)
# try:
#     model = pickle.load('./model/iris_model.pkl')
#     print("Model loaded successfully!")
# except Exception as e:
#     print(f"Error loading model: {e}")
#     model = None

with open('./model/iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Flask Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    try:
        data = request.get_json()
        
        # Validate input
        if not data or not isinstance(data, dict):
            return jsonify({"error": "Invalid input format"}), 400
            
        # Convert values to float safely
        try:
            features = [float(x) for x in data.values()]
        except (ValueError, TypeError):
            return jsonify({"error": "All values must be numeric"}), 400

        # Debug print
        print("Received features:", features)
        
        # Convert to numpy array and reshape for prediction
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_array)[0]
        
        return jsonify({
            "prediction": float(prediction),  # Ensure JSON serializable
            "status": "success",
            "input_features": features
        }), 200
        
    except Exception as e:
        print(f"Prediction error: {e}")
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)