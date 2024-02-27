# AIRA CATIG
# RCATIG@UCI.EDU
# 85952906

import socket
from ds_protocol import DSPProtocol

ADDRESS = "168.235.86.101"
PORT = 3021
JOIN = "join"
POST = "post"
BIO = "bio"
ERROR = "error"
OK = "ok"

def send(server: str, port: int, username: str,
         password: str, message: str, bio: str = None):
    """
    The send function joins a ds server and sends a message, bio, or both
    :param server: The ip address for the ICS 32 DS server.
    :param port: The port where the ICS 32 DS server is accepting connections.
    :param username: The user name to be assigned to the message.
    :param password: The password associated with the username.
    :param message: The message to be sent to the server.
    :param bio: Optional, a bio for the user.
    """
    # TODO: return either True or False depending
    # on results of required operation
    try:
      client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client.connect((ADDRESS, PORT))
      if message == None and bio == None:
        p = DSPProtocol(username, password)
        message = p.join(username, password)
        #msg = '{"token":"4678397c-6106-4046-aa13-2acd87ef540c", "post": {"entry": "Hello World!","timestamp": 1708989068.9272954}}'
        send = client.makefile("w")
        recv = client.makefile("r")
        send.write(message + "\r\n")
        send.flush()
        resp = recv.readline()
        print(resp)
        print(p.extract_json(resp)[2])
        #print(get_token(token))
        client.close()
      #elif bio == None:
    except:
        pass


def get_token(user_token=None):
    token = ""
    if token != None:
        token += user_token
    return token
  

#send(ADDRESS, PORT, "silverstone", "fast", None)
send(ADDRESS, PORT, "silverstone", "fast", None)