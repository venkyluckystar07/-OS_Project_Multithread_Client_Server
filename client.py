import socket
from os.path import exists as file_exists
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "DISCONNECT"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client.connect(ADDR)  #connects client to the server 
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    
    connected = True
    while connected:
        msg =input("Enter the url you want to search  or DISCONNECT to stop the connection")
        client.send(msg.encode(FORMAT))
        if msg == DISCONNECT_MSG:
            connected = False
        else:
            filename=filexists()
            
            client.send(filename.encode(FORMAT))
            msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER] {msg}")


def filexists():
    filename=input("Enter the name of file of webpage you want to save")   
    filename=filename+'.html'   
    while file_exists(filename):
         print("file already exits/n")
         filename=input("Enter the name of file of webpage you want to save") 
         filename=filename+'.html'  

    return filename




if __name__ == "__main__":
    main()


