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
    def __init__(self, user:str, password: str, bio: str=None):
        self.user = user
        self.password = password
        self.bio = bio
    
    def join(self, user:str, password:str):
        result = {"join": {"username": user, "password": password, "token": ":"}}
        return json.dumps(result)

    def post(self, entry:str, token: str):
        timestamp = time.time()
        result = {"token":token,"post":{"entry":entry,"timestamp":timestamp}}
        return json.dumps(result)
    
    def bio(self, token:str, entry:str, timestamp: int) -> dict:
        result = {"token":token,"bio":{"entry":entry,"timestamp":timestamp}}
        return json.dumps(result)
    
    def error(self, error, message):
        result = {"response":{"type":error,"message":message}}
        return json.dumps(result)
    
    def ok(self, error, message, token):
        result = {"response":{"type":error,"message":message,"token":token}}
        return json.dumps(result)
    
def extract_json(json_msg: str) -> DataTuple:
    """
    Call the json.loads function on a json string
    and convert it to a DataTuple object
    TODO: replace the pseudo placeholder keys with actual DSP protocol keys
    """
    try:
        json_obj = json.loads(json_msg)
        join = json_obj["join"]
        post = json_obj["post"]
        bio = json_obj["bio"]
        error = json_obj["error"]
        ok = json_obj["ok"]
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return DataTuple(join, post, bio, error, ok)
