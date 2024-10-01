import os
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from src.model import build_model

# Initialize Flask app
app = Flask(__name__)

# Define the path to save uploaded images temporarily
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Path to pre-trained model
MODEL_PATH = os.path.join(os.getcwd(), 'models', 'saved_model.keras')

# Load the pre-trained model
model = None

def load_trained_model():
    global model
    model = build_model()  # Use the build_model function from src.model
    model.load_weights(MODEL_PATH)

# Load the model once when the app starts
load_trained_model()

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    # Load and preprocess the image
    image = load_img(image_path, target_size=(512, 512))  # Resize to match model input
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image / 255.0  # Normalize to [0, 1]
    return image

# Define your class names
class_names = ['Jaguar', 'Stratocaster', 'Telecaster']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file and allowed_file(file.filename):
            # Save the file temporarily
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            # Preprocess the image
            image = preprocess_image(file_path)

            # Make a prediction
            predictions = model.predict(image)

            # Post-process the prediction
            predicted_class = np.argmax(predictions, axis=1)[0]
            confidence = np.max(predictions)

            # Map predicted class to class name
            predicted_class_name = class_names[predicted_class]

            # Clean up the uploaded file
            os.remove(file_path)

            # Return the result as JSON
            return jsonify({
                'predicted_class': predicted_class_name,  # Use class name
                'confidence': float(confidence)
            })

        return jsonify({"error": "Invalid file format"}), 400

    return render_template('index.html')


# Static folder setup for serving CSS and JS
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(debug=True)
