# ds_protocol.py

# AIRA CATIG
# RCATIG@UCI.EDU
# 85952906

import json
from collections import namedtuple
import time


class DSPProtocol:
    """
    Format protocol to send to online server as 
    a dictionary.
    """
    def __init__(self, user: str = None, password:
                 str = None, bio: str = None):
        self.user = user
        self.password = password

    def join(self, user: str, password: str):
        """
        Create message as a dictionary with a 
        username, password, and token generated
        from the server to join the server.
        """
        result = {"join": {"username": user,
                  "password": password, "token": ":"}}
        return json.dumps(result)

    def post(self, token: str, entry: str):
        """
        Create message as a dictionary with the
        post entry, token from the server, and timestamp
        to post the entry to the server.
        """
        timestamp = time.time()
        result = {"token": token, "post": {"entry":
                  entry, "timestamp": timestamp}}
        return json.dumps(result)

    def bio(self, token: str, entry: str):
        """
        Create message as a dictionary with the bio
        entry, token from the server, and timestamp 
        to add bio the server.
        """
        timestamp = time.time()
        result = {"token": token, "bio": {"entry": entry,
                  "timestamp": timestamp}}
        return json.dumps(result)

    def error(self, error, message):
        """
        Create message as a dictionary that will return
        the type of error along with the error message.
        """
        result = {"response": {"type": error, "message": message}}
        return json.dumps(result)

    def ok(self, error, message, token):
        """
        Create message as a dictionary after each message
        sent to the server is allowed. Will include the type,
        message, and token recieved from server.
        """
        result = {"response": {"type": "ok", "message":
                  message, "token": token}}
        return json.dumps(result)


DataTuple = namedtuple("DataTuple", ["type", "message", "token"])


def extract_json(json_msg: str) -> DataTuple:
    """
    Call the json.loads function on a json string
    and convert it to a DataTuple object
    """
    try:
        json_obj = json.loads(json_msg)
        protocol_type = json_obj["response"]["type"]
        message = json_obj["response"]["message"]
        token = json_obj["response"]["token"]
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return DataTuple(protocol_type, message, token)
