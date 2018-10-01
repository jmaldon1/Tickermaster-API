from flask import Flask, jsonify, request
from keys import ticketmasterAPIKey
import requests
import json
app = Flask(__name__)

apikey = ticketmasterAPIKey
search_url = "https://app.ticketmaster.com/discovery/v2/events.json"

@app.route("/")
def hello():
	return jsonify({"about":"Hello World!"})

@app.route("/get_events", methods=['GET','POST'])
def events():

	if request.method == 'POST':
		#store the file that is passed in with the POST request
		file = request.files['file']
		data = json.load(file)
	else: #For debugging, if script.py didnt make a POST request, just manually load the file
		with open('request.json') as f:
			data = json.load(f)

	#Payload that will be sent to the ticketmaster API
	payload = {"postalCode":data['postalCode'],"startDateTime":data['startDateTime'],"endDateTime":data['endDateTime'], "city":data['city'], "apikey":apikey}
	#Make a request to the ticketmaster api given the URL and the parameters
	search = requests.get(search_url, params=payload)
	#Turn response into json
	search_json = search.json()

	return jsonify(search_json)

if __name__ == '__main__':
	app.run(debug=True)

