# AIRA CATIG
# RCATIG@UCI.EDU
# 85952906

import socket
from ds_protocol import DSPProtocol, extract_json

ADDRESS = "168.235.86.101"
PORT = 3021
JOIN = "join"
POST = "post"
BIO = "bio"
ERROR = "error"
OK = "ok"
token = None


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
        if message is None and bio is None:  # User is trying to send a join message
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((server, port))
            protocol = DSPProtocol()
            client_message = protocol.join(username, password)
            send = client.makefile("w")
            recv = client.makefile("r")
            send.write(client_message + "\r\n")
            send.flush()
            resp = recv.readline().strip()
            print(resp)
            token = extract_json(resp)[2]
            get_token(token)
            client.close()
        elif bio is None:  # User is trying to send a post message
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((server, port))
            token = get_token()
            protocol = DSPProtocol()
            client_message = protocol.post(token, message)
            send = client.makefile("w")
            recv = client.makefile("r")
            send.write(client_message + "\r\n")
            send.flush()
            resp = recv.readline().strip()
            print(resp)
            client.close()
        elif bio is not None and message is None:  # User is trying to send a bio message
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((server, port))
            token = get_token()
            protocol = DSPProtocol()
            client_message = protocol.bio(str(token), bio)
            send = client.makefile("w")
            recv = client.makefile("r")
            send.write(client_message + "\r\n")
            send.flush()
            resp = recv.readline().strip()
            print(resp)
            client.close()
        return True
    except TypeError:
        pass


def get_token(user_token=None):
    """
    Recieve token for each connection
    to the online server.
    """
    global token
    if user_token is not None:
        token = user_token
    return token
