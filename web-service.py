# https://www.tensorflow.org/guide/keras/save_and_serialize - loading the model

# flask for web app.
from flask import Flask ,request, render_template

# numpy for numerical work.
import numpy as np
# Tensorflow for keras
import tensorflow as tf
from tensorflow import keras

# Create a new web app.
app = Flask(__name__)

# Add root route.
@app.route("/")
def home():
    
  return render_template('index.html')

# Making a route to get the input from form in index.html
@app.route("/send", methods=['POST', 'GET'])
def send():
  predict_data = 0
  
  # To verify the request is a post
  if request.method == 'POST':
    
    dataset = pd.read_csv("https://raw.githubusercontent.com/ianmcloughlin/2020A-machstat-project/master/dataset/powerproduction.csv")
    
    # Adding the prediction input from index.html
    prediction = np.array(float(request.form.get('prediction')))
    
    dataset_features = dataset.copy()
    dataset_features = np.array(dataset_features)
    dataset_power = dataset_features.pop('power')
    dataset_power = np.array(dataset_power)
    
    # Loading the saved model
    data_model = keras.models.load_model("model.h5")

    # Making a prediction
    predict_data= data_model.predict(prediction)
  
  return render_template('index.html', predict_data = predict_data)
