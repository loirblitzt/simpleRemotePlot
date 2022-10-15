import socket
import sys

HOST, PORT = "localhost", 31300
data = " ".join(sys.argv[1:])
# data = "n"*102

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8")) # \n serves as a EOF character

print("Sent:     {}".format(data))
# print("Received: {}".format(received))