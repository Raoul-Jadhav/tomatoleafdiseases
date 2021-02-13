# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:01:17 2020

@author: RAHUL
"""
from __future__ import division, print_function
import numpy as np 
import sys
import os
import re
import glob

# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image 

# Flask utils
from flask import Flask, request, url_for, redirect, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app=Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'model_inception.h5'    # Assigning our model name to model path variable.

# Loading Model
model = load_model(MODEL_PATH)
#model._make_predict_function()  # Inbuilt function 

### Preprocessing Function
def model_predict(img_path,model):
    img=image.load_img(img_path,target_size=(224,224))
    
    # Preprocessing the image, converting imageto array
    x = image.img_to_array(img)    
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
    
    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    if preds == 0:
        preds="Bacterial spot"
    elif preds==1:
          preds="Early blight"
    elif preds==2:  
          preds="Late blight"
    elif preds==3:  
          preds="Leaf Mold"    
    elif preds==4:  
          preds="Septorial leaf spot"    
    elif preds==5:  
          preds="Spider mites two spotted spider mites"
    elif preds==6:  
          preds="Target spot"
    elif preds==7:  
          preds="Yellow leaf curl virus"
    elif preds==8:  
          preds="Mosaic virus"
    elif preds==9:  
          preds="Healthy"
    return preds
  


# Routing 
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        return result
    return 'Error'
    

if __name__=='__main__':
    app.run(debug=True)    
    