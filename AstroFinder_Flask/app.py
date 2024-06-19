import os
import numpy as np
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model
model = load_model('prev_model.h5')

# Define the class categories
categories = ['nebula', 'none', 'asteroids', 'galaxies']

def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0  # Normalize pixel values
    img_batch = np.expand_dims(img_array, axis=0)
    return img_batch

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # Prepare the image
        img_batch = prepare_image(file_path)

        # Make prediction
        predictions = model.predict(img_batch)
        predicted_class_index = np.argmax(predictions)
        predicted_class = categories[predicted_class_index]

        return jsonify({'predicted_class': predicted_class})

if __name__ == '__main__':
    # Create uploads directory if not exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(host='0.0.0.0', port=5000, debug=False)
