import requests
import json
from flask import Flask,redirect,render_template,request,url_for
 
app = Flask(__name__)

@app.route('/')
def my_form():
    return redirect(url_for('form'))

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data', methods=['POST'])
def data():

        SurveyTxt = request.form.get('Response')
    
        headers = {
            'Authorization': 'Bearer ya29.c.KqYBDQgboS_t9R_WrGUXbMj7gI3poW7gJfbQIHI8oiBvikzhyzYI5MBanH0OKjRjNM7eXIjjh0Br_ZNOpVxjzJaZo3SAPsdoHB2xE8wlrO3qAeL-6n_9vS3-ivrmcj_r1L53MgGDE7aOmPmGgDr4LVIh7hmNNm6p86dZz5ZaMIwwHKJ6X65kB4W10QdeTaO0y0npYzdO8f0clae5j3d48Lhf8qhZ5ghkgw',
            'Content-Type': 'application/json',
                  }

        a_file = open("request.json", "r")
        json_object = json.load(a_file)
        a_file.close()
  
        json_object["payload"]["textSnippet"]["content"] = SurveyTxt
        
        a_file = open("request.json", "w")
        json.dump(json_object, a_file)
        a_file.close()

        payload = open('request.json')

        response = requests.post('https://automl.googleapis.com/v1/projects/536885716547/locations/us-central1/models/TST2306007935957860352:predict', headers=headers , data=payload) 

        surv_result = response.json()

        surv_result_disp = surv_result["payload"][0]["textSentiment"]  #first check if negative sentiment 

        if len(surv_result_disp) < 1:         #json returns {} for negative sentiment
            surv_result_disp = 'Negative'

        else:
            surv_result_disp = surv_result["payload"][0]["textSentiment"]["sentiment"]  #get json response sentiment for positive or neutral

            if surv_result_disp == 1:
                surv_result_disp = 'Neutral'

            if surv_result_disp == 2:
                surv_result_disp = 'Positive'

        surv_result_sentiment = surv_result["metadata"]["sentiment_score"]          #get json response sentiment score

        surv_result_final = surv_result_disp + " with a sentiment score of " + surv_result_sentiment

        return render_template('data.html',form_data = surv_result_final)
 
app.run(host='127.0.0.1', port=8080, debug=True)
