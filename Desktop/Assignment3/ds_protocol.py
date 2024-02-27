# ds_protocol.py

# AIRA CATIG
# RCATIG@UCI.EDU
# 85952906

import json
from collections import namedtuple
import Profile
import time




# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple("DataTuple", ["join", "post", "bio", "error","ok"])

class DSPProtocol:
    def __init__(self, user:str=None, password: str=None, bio: str=None):
        self.user = user
        self.password = password
    
    def join(self, user:str, password:str):
        result = {"join": {"username": user, "password": password, "token": ":"}}
        return json.dumps(result)

    def post(self, token: str, entry: str):
        timestamp = time.time()
        result = {"token":token,"post":{"entry":entry,"timestamp":timestamp}}
        return json.dumps(result)
    
    def bio(self, token:str, entry:str):
        print("hi")
        timestamp = time.time()
        result = {"token":token,"bio":{"entry":entry,"timestamp":timestamp}}
        return json.dumps(result)
    
    def error(self, error, message):
        result = {"response":{"type":error,"message":message}}
        return json.dumps(result)
    
    def ok(self, error, message, token):
        result = {"response":{"type":error,"message":message,"token":token}}
        return json.dumps(result)
    
DataTuple = namedtuple("DataTuple", ["type", "message", "token"])
def extract_json(json_msg: str) -> DataTuple:
    """
    Call the json.loads function on a json string
    and convert it to a DataTuple object
    TODO: replace the pseudo placeholder keys with actual DSP protocol keys
    """
    try:
        json_obj = json.loads(json_msg)
        protocol_type = json_obj["response"]["type"]
        message = json_obj["response"]["message"]
        token = json_obj["response"]["token"]
        #ok = json_obj["ok"]
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return DataTuple(protocol_type, message, token)
