# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

# Import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 5500
serverSocket.bind(("127.0.0.1", serverPort))
serverSocket.listen(1)
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # FILL IN START		# FILL IN END
    try:
        message = connectionSocket.recv(1024).decode()
        filepath = message.split()[1]
        f = open(filepath[1:])
        outputdata = f.read()  # FILL IN START		# FILL IN END
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        response = outputdata + "\r\n"
        connectionSocket.send(response.encode())  # Python 3
        connectionSocket.close()
    except (IOError, IndexError):
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.send(
            "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        connectionSocket.close()


serverSocket.close()
