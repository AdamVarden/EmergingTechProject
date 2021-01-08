# Emerging Tech Project
Adam Varden - G00359605


## Running the web-service
### Run the following commands in the command prompt.
> set FLASK_APP=web-service.py

> python -m flask run

### View the index.html in browser
> Copy this link and enter into url line in a brower:
> http://127.0.0.1:5000/

### Running the Dockerfile
> Open a command prompt in the directory the dockerfile is in and run the following commands:

> docker build . -t model-image

> docker run --name model-container -d -p 5000:5000 model-image

I used this video and this repo to learn how to use docker
> Video: https://web.microsoftstream.com/video/03bfee62-fdeb-4dbe-a7d2-393d1aa40b66

> Repo: https://github.com/ianmcloughlin/random-app

### The model.h5 file
This file is created from the the jupyter notebook and is used to load the trained data model into the web-service. The purpose of the .h5 file is to store store the weights and model configuration in a file
>https://stackoverflow.com/questions/48320588/what-is-h5-model-in-keras

### Errors
When the web service loads an internal server error appears that is due to 
the prediction value being entered into the model prediction function and the list being out of range.
