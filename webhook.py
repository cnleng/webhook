from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os, requests, collections, time
import pickle

app = Flask(__name__)
CORS(app)

PUT = "PUT"
POST = "POST"
GET = "GET"
PATCH = "PATCH"

@app.route("/api/v1/posts", methods=['GET'])
def default():
    posts = [{'id': 1, 'title': 'hello world!', 'body': 'post body'}]
    return jsonify(posts)

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
