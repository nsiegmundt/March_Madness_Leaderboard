from flask import Flask, render_template, request, jsonify
from random import randint
import requests
import json
import io

app = Flask(__name__, static_url_path='/static')

# Handles GET requests
@app.route('/', methods=['GET'])
def index():
    # Render page
    return render_template('index.html', title='Home')

@app.route('/get-score')
def espnGet():
    firstCheck = request.args.get('firstCheck')
    # firstCheck = "false"
    
    groupEndpoint = "http://fantasy.espncdn.com/tournament-challenge-bracket/2019/en/api/group?groupID=2853834&sort=-1&start=0&length=50&periodPoints=true"
    
    response = requests.get(url=groupEndpoint)
    dataArray = response.json()['g']['e']
    
    # If we are checking this data for the first time, assume its day1 data
    if firstCheck == "true":
        day1Data = {}
        
        for data in dataArray:
            day1Data[data["n_e"]] = data['pp']['6']
            # day1Data[data["n_e"]] = randint(150, 250) * -1
         
        with io.open('data1_data.txt', 'w', encoding='utf8') as outfile:  
            json.dump(day1Data, outfile)
        
        return jsonify({"day1Data": day1Data, "currentData": dataArray})
    else:
        day1Data = []
        
        with io.open('data1_data.txt', encoding='utf8') as json_file:  
          day1Data = json.load(json_file)
          
        return jsonify({"day1Data": day1Data, "currentData": dataArray})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
