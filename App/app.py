from flask import Flask, request
import requests
import nltk
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/api',methods=['GET'])
def getLocationWeather():
    inputChar = str(request.args['query'])
    result = inputChar.title()
    Ne_sent = result
    Ne_tokens = nltk.word_tokenize(Ne_sent)
    Ne_tags = nltk.pos_tag(Ne_tokens)
    location_name = ""

    for words in Ne_tags:
        if(words[1] == 'NNP'):
            location_name = words[0]
    
    apiKey = os.getenv("apiKey")
    completeUrl = "https://api.openweathermap.org/data/2.5/weather?q=" +location_name+"&appid="+apiKey
    response = requests.get(completeUrl)
    return response.json()


if __name__ == "__main__":
     app.run()
