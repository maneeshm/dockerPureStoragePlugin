import logging
import json
from flask import request
from logging.handlers import RotatingFileHandler
from flask import Flask
import flask
from inspect import currentframe, getframeinfo
app = Flask(__name__)

@app.route('/Plugin.Activate', methods=["POST"])
def plugin_activate():
    app.logger.info("hello world")
    return flask.make_response(json.dumps({
            "Implements": ["VolumeDriver"]
           }), 200)

@app.route('/VolumeDriver.Create', methods=["POST"])
def volumeDriverCreate():
    app.logger.info("volumeDriverCreate")
    json_req = json.loads(request.data)
    app.logger.info("Request data " + request.data)
    app.logger.info("Volume name is " + json_req.get("Name"))
    return flask.make_response(json.dumps({
            "Err": ""
           }), 200)

@app.route('/VolumeDriver.Remove', methods=["POST"])
def volumeDriverRemove():
    app.logger.info("VolumeDriver.Remove")
    json_req = json.loads(request.data)
    app.logger.info("Request data " + request.data)
    app.logger.info("Volume name is " + json_req.get("Name"))
    return flask.make_response(json.dumps({
            "Err": ""
           }), 200)

@app.route('/VolumeDriver.Mount', methods=["POST"])
def volumeDriverMount():
    app.logger.info("VolumeDriver.Mount")
    json_req = json.loads(request.data)
    frameinfo = getframeinfo(currentframe())
    app.logger.info("Request data " + request.data)
    app.logger.info(frameinfo.filename + str(frameinfo.lineno))
    app.logger.info("Volume name is " + json_req["Name"])
    app.logger.info("Volume ID is " + str(json_req.get("ID")))
    return flask.make_response(json.dumps({
            "Mountpoint" : "/root/flaskPy/myfile.img",
            "Err": ""
           }), 200)

@app.route('/VolumeDriver.Path', methods=["POST"])
def volumeDriverPath():
    app.logger.info("VolumeDriver.Path")
    json_req = json.loads(request.data)
    app.logger.info("Request data " + request.data)
    app.logger.info("Volume name is " + json_req["Name"])
    return flask.make_response(json.dumps({
            "Mountpoint" : "/root/flaskPy/myfile.img",
            "Err": ""
           }), 200)

@app.route('/VolumeDriver.Unmount', methods=["POST"])
def volumeDriverUnmount():
    app.logger.info("VolumeDriver.Unmount")
    json_req = json.loads(request.data)
    app.logger.info("Request data " + request.data)
    app.logger.info("Volume name is " + json_req["Name"])
    app.logger.info("Volume ID is " + json_req["ID"])
    return flask.make_response(json.dumps({
            "Err": ""
           }), 200)

@app.route('/VolumeDriver.Get', methods=["POST"])
def volumeDriverGet():
    app.logger.info("VolumeDriver.Get")
    json_req = json.loads(request.data)
    app.logger.info("Request data " + request.data)
    vol_name = json_req["Name"]
    app.logger.info("Volume name is " + vol_name)
    return flask.make_response(json.dumps({
            "Volume" : {
                         "Name" : vol_name,
                         "Mountpoint" : "/root/flaskPy/myfile.img",
                         "Status" : {}
                       },
            "Err": ""
           }), 200)

@app.route('/VolumeDriver.List', methods=["POST"])
def volumeDriverList():
    app.logger.info("VolumeDriver.List")
    app.logger.info("Request data " + request.data)
    return flask.make_response(json.dumps({
            "Volumes" : [{
                         "Name" : vol_name,
                         "Mountpoint" : "/root/flaskPy/myfile.img",
                       }],
            "Err": ""
           }), 200)

@app.route('/VolumeDriver.Capabilities', methods=["POST"])
def volumeDriverCapabilities():
    app.logger.info("VolumeDriver.Capabilities")
    app.logger.info("Request data " + request.data)
    return flask.make_response(json.dumps({
                 "Capabilities": {
                           "Scope": "global"
                       }
           }), 200)

if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    app.run()
