# Assignment 3 - Publishing Online

Assignment 3 is an addition to the Assignment 1 and Assignment 2 with a new feature of not just saving a profile on a local computer, but sending the data of profile to the Internet using a server. After either creating a new file or opening a file, users are prompted the option to send the username, password, and bio to the server to be posted on the Internet. Users are also prompted to do the same after creating a new post. Once the data is sent to the server, a user can view their profile along with their saved bio and collection of posts. Assignment 3 is divided into five modules which include a3.py, ui.py, ds_protocol.py, ds_client.py, and Profile.py.

Within a3.py, it includes the main enterance into the program and prompts the user if they would like to create or open a file, which is then operated through ui.py. Ui.py contains all of the functions to send data to the server. Ds_protocol.py formats the messages into a specific format that allows the server to recieve and read the messages sent. Ds_client.py is the module that contains the send function which connects to the server and sends all the messages. Profile.py contains the classes to create any profiles and saves the ip address the user inputs.


Team Members:
Aira Catig
rcatig@uci.edu