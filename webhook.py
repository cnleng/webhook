from flask import Flask, request
import json, os, requests, collections, time
import pickle
app = Flask(__name__)

PUT = "PUT"
POST = "POST"
GET = "GET"
PATCH = "PATCH"

@app.route("/api/v1/", methods=['GET'])
def default():
    message = {'message': 'hello world!'}
    return message

@app.route("/api/v1/webhook/", methods=['POST'])
def notification():
    notification = json.loads(request.data)
    now = time.time()
    with open('notification_file_{}.json'.format(now), 'wb') as f:
        pickle.dump(notification, f)
        #json.dump(request.data,f)
    print(notification)
    return 'OK'

if __name__ == '__main__':
   app.run(host='0.0.0.0')
