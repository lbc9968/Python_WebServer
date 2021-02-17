#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)

   #Prepare a sever socket
   #Fill in start
   # Bind the socket to server address and server port
   serverSocket.bind(("", port))

   # Listen to at most 1 connection at a time
   serverSocket.listen(1)
   #Fill in end
   # Server should be up and running and listening to the incoming    connections
   while True:
       #Establish the connection
       #print('Ready to serve...')
       # Fill in start
       connectionSocket, addr =  serverSocket.accept()
       # #Fill in end
       try:
           message = connectionSocket.recv(1024) #Fill in start    #Fill in end
           #print(message)
           if len(message)>0 :
            filename = message.split()[1]
            #print(filename)
            f = open(filename[1:])
            outputdata = f.read()
            #Fill in start     #Fill in end
            #print(outputdata)

            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n", "UTF-8"))
            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
       except IOError:
           #Send response message for file not found (404)
           #Fill in start
           connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
           connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n", "UTF-8"))
           #Fill in end

           #Close client socket
           #Fill in start
           connectionSocket.close()

           #Fill in end

   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)

