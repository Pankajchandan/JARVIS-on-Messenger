import os

import requests

import config
from templates.text import TextTemplate

from clarifai import rest
from clarifai.rest import ClarifaiApp

CLARIFAI_API_KEY = os.environ.get('CLARIFAI_API_KEY', config.CLARIFAI_API_KEY)
#CLARIFAI_API_KEY = 'f510238c77d04f2fb4356b8ec676f453'
print CLARIFAI_API_KEY

def process(input, entities=None):
    #import model
    app = ClarifaiApp(api_key=CLARIFAI_API_KEY)
    model = app.models.get("general-v1.3")
    
    #predict value
    val1 = model.predict_by_url(url=input)["outputs"][0]["data"]["concepts"][0]["name"]
    val2 = model.predict_by_url(url=input)["outputs"][0]["data"]["concepts"][1]["name"]
    val3 = model.predict_by_url(url=input)["outputs"][0]["data"]["concepts"][2]["name"]
    msg = "looks like "+val1+"."+" Might be "+val2+" as well or "+val3
    
    #pack output
    output = {
        'input': input,
        'output': TextTemplate(msg).get_message(),
        'success': True
    }
    return output