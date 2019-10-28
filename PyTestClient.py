#!/usr/bin/env python3
import requests
from flask import Flask, jsonify, request, Request
app = Flask(__name__)

@app.route("/", methods=["POST"])
def accept():
    # Request.
    body = request.get_json()
    print(body)
    return jsonify("Hello")

hubHost = "localhost"

def PostResult(Host, Payload, port = 20000, Uri = None):
    try:
        if Uri == None:
            Uri = "http://" + Host + ":" + str(port) + "/MachineMessageApi"
        r = requests.post(Uri, json=Payload)
        return True
    except:
        return False

if __name__ == "__main__":
    res = PostResult(hubHost, "AddMachineMessageSubscriber,127.0.0.1,5008")
    print("Subscribed:", res)
    app.run(port=5008)