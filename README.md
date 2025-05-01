# AstroFinder

AstroFinder is a deep learning project that classifies space objects into four categories: galaxies, asteroids, nebulae, and none. The project includes a Jupyter notebook for model training and evaluation, a Flask web application for image classification, and a pre-trained model file.

https://github.com/avgvcoding/AstroFinder/assets/136979087/4929cb72-c001-4952-af29-a453daf6db8e

## Project Structure
- **Video_demo.mp4**: It contains video demonstration of website with model prediction and image uploading capabilities.
- **AstroFinder.ipynb**: Jupyter notebook for training and evaluating the deep learning model.
- **AstroFinder_Flask/**: Directory containing the Flask web application.
  - **app.py**: Flask application code for serving the model and handling image uploads.
  - **templates/**: Directory containing HTML templates.
    - **index.html**: The main HTML file for the web interface.
  - **prev_model.h5**: Pre-trained model file.

## Features

- **Image Classification**: Classifies images of space objects into galaxies, asteroids, nebulae, and none.
- **Web Interface**: User-friendly web application for uploading images and viewing predictions.
- **Pre-trained Model**: A pre-trained model ready for deployment.

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AstroFinder.git
cd AstroFinder
```

### 2. Install Dependencies

Navigate to the `AstroFinder_Flask` directory and install the required Python packages:

```bash
cd AstroFinder_Flask
pip install -r requirements.txt
```

### 3. Run the Flask Application

```bash
python app.py
```

### 4. Access the Web Application

Open your web browser and navigate to `http://127.0.0.1:5000` to access the web interface.

## Usage

### Jupyter Notebook

1. Open `AstroFinder.ipynb` in Jupyter Notebook or Jupyter Lab.
2. Run the cells to train and evaluate the deep learning model.

### Flask Web Application

1. Start the Flask application as described in the setup section.
2. Use the web interface to upload an image and get the prediction of the space object category.

## Model Details

The deep learning model is a Convolutional Neural Network (CNN) designed to classify images of space objects. The model was trained on a dataset of labeled images of galaxies, asteroids, and nebulae. It takes an input image of size 128x128 pixels and outputs the probabilities for each category.



