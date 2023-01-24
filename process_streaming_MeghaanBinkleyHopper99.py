"""

Streaming Process - port 9999

Data found here: https://www.kaggle.com/datasets/pavelbiz/monthly-btc-rate-from-2014-to-present

"""

import csv #Enables Python to read the csv file
import socket #Allows python to communicate with UDP socket
import time #Allows for time delay

host = "localhost"
port = 9999
address_tuple = (host, port)

# use an enumerated type to set the address family to (IPV4) for internet
socket_family = socket.AF_INET 

# use an enumerated type to set the socket type to UDP (datagram)
socket_type = socket.SOCK_DGRAM 

# use the socket constructor to create a socket object we'll call sock
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# read from a file from kaggle.com
input_file = open("BTC-USD.csv", "r")

# use the built in sorted() function to get them in chronological order
reversed = sorted(input_file)

# create a csv reader for our comma delimited data
reader = csv.reader(reversed, delimiter=",")

for row in reader:
    # read a row from the file
    D, O, H, L, C, A, V = row

    # use an fstring to create a message from our data
    # notice the f before the opening quote for our string?
    fstring_message = f"[{D}, {O}, {H}, {L}, {C}, {A}, {V}]"
    
    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()

    # use the socket sendto() method to send the message
    sock.sendto(MESSAGE, address_tuple)
    print (f"Sent: {MESSAGE} on port {port}.")

    # 2 second delay
    time.sleep(2)
