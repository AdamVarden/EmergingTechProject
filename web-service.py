# https://www.tensorflow.org/guide/keras/save_and_serialize - loading the model
# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  
  data_model = keras.models.load_model("model")
  return app.send_static_file('index.html')
