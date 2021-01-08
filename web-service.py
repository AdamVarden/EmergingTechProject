# References
# https://www.tensorflow.org/guide/keras/save_and_serialize - loading the model

# https://www.youtube.com/watch?v=1k3cNPWVpcY&t=994s&ab_channel=CodingFuture - Sending data between the html file and the web service
# https://web.microsoftstream.com/video/05d8b607-56c3-44a8-9539-c940257e43d8 - learning to use flask

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
  # Using templates made it easier to return data rather than static
  return render_template('index.html')

# Making a route to get the input from form in index.html
@app.route("/send", methods=['POST', 'GET'])
def send():
  predict_data = 0
  
  # To verify the request is a post
  if request.method == 'POST':

    #Adding prediction to an array
    prediction = np.array(float(request.form.get('prediction')))
    
    # Loading the saved model
    data_model = keras.models.load_model("model.h5")

    # Making a prediction
    predict_data= data_model.predict(prediction)
  
  return render_template('index.html', predict_data = predict_data)
