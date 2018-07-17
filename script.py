import requests
import json
import datetime
import boto3
from botocore.client import Config
from keys import AWSKeyID, AWSSecretKey

ACCESS_KEY_ID = AWSKeyID
ACCESS_SECRET_KEY = AWSSecretKey
BUCKET_NAME = 'ticketmaster-api'

#Current Time
time = str(datetime.datetime.now()).replace(" ", "_")
#URL to make POST request
url = "http://localhost:5000/get_events"

#puts file into format that can be sent to POST request
files = {'file': open('request.json','rb')}

#make the POST request
r = requests.post(url, files=files)
#convert to json
r_json = r.json()

#store file name when the file is created
filename = 'data{}.json'.format(time)

#write json data to file
with open(filename, 'w') as outfile:
    json.dump(r_json, outfile)

#stores file data
data = open(filename, 'rb')

#boto s3 config
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
#creates an S3 object
s3.Bucket(BUCKET_NAME).put_object(Key='{}/{}'.format(time, filename), Body=data)

print ("Uploaded")