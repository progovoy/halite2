import socket
import sys

# Connect
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', int(sys.argv[1])))
socket.listen(1)
connection, _ = socket.accept()

# IO Functions
def sendStringPipe(toBeSent):
    sys.stdout.write(toBeSent+'\n')
    sys.stdout.flush()

def getStringPipe():
    s = sys.stdin.readline().rstrip('\n')
    return(s)

def sendStringSocket(toBeSent):
    global connection
    toBeSent += '\n'
    connection.sendall(bytes(toBeSent, 'ascii'))

def getStringSocket():
    global connection
    newString = ""
    buf = '\0'
    while True:
        buf = connection.recv(1).decode('ascii')
        if buf != '\n':
            newString += str(buf)
        else:
            return newString

# Handle Init IO
sendStringSocket(getStringPipe()) # Player ID
sendStringSocket(getStringPipe()) # Map Dimensions
sendStringSocket(getStringPipe()) # Starting map
sendStringPipe(getStringSocket()) # Player Name / Ready Response

# Run Frame Loop
while True:
    sendStringSocket(getStringPipe()) # Frame Map
    sendStringPipe(getStringSocket()) # Move List
