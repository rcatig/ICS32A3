# ds_protocol.py

# AIRA CATIG
# RCATIG@UCI.EDU
# 85952906

import json
from collections import namedtuple
import Profile


JOIN = "join"
POST = "post"
BIO = "bio"

# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple("DataTuple", ["username", "password", "message", "bio"])


def extract_json(json_msg: str) -> DataTuple:
    """
    Call the json.loads function on a json string
    and convert it to a DataTuple object
    TODO: replace the pseudo placeholder keys with actual DSP protocol keys
    """
    try:
        json_obj = json.loads(json_msg)
        username = json_obj["username"]
        password = json_obj["password"]
        message = json_obj["message"]
        bio = json_obj["bio"]
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return DataTuple(username, password, message, bio)
