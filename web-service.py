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

@app.route("/send", methods=['POST', 'GET'])
def send():
  predict_data = 0
  if request.method == 'POST':
    prediction = float(request.form.get('prediction'))
    data_model = keras.models.load_model("model.h5")
    predict_data= data_model.predict(prediction)
  
  return render_template('index.html', predict_data = predict_data)
