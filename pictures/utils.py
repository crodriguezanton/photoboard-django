import socket


def call_socket(uuid):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), 8008))
    serversocket.listen(5)

    (clientsocket, address) = serversocket.accept()

    if clientsocket.recv(10) == "CONN":
        print "Sending UUID: " + uuid
        clientsocket.send(uuid)
        print clientsocket.recv(2)

    clientsocket.close()
    serversocket.close()

