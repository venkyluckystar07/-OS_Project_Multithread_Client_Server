import socket    # one end point to a two way communication link
import threading #to handle multiple clients simentaneously 

from urllib.request import urlopen #to open url and read source code from url



IP = socket.gethostbyname(socket.gethostname())   
PORT = 5566
ADDR = (IP, PORT)  #binding ip and port as a tuple
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "DISCONNECT"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")  #whenever a new client is connected

    connected = True
    while connected:  #when a server recievs a disconnet commant it will be out of a loop
        url = conn.recv(SIZE).decode(FORMAT) #decoding msg from client
       
        if url == DISCONNECT_MSG:  #if client sent msg to disconnect
            connected = False   
            print(f"client{addr} was disconnected ")
            continue
        filename=conn.recv(SIZE).decode(FORMAT) #decoding the filename
        print(f"client{addr} sent url {url} ")  
        print(f"client{addr} sent filename as {filename} ")
        with urlopen(url) as response:   #opening the url 
             html_response = response.read()  #reading the source code
             encoding = response.headers.get_content_charset('utf-8')  #encoding the souce code to a readable format
             decoded_html = html_response.decode(encoding) #converting the httpResponse as a string to write in file
        with open(filename, 'w') as f:  #opning and write the source code 
           f.write(decoded_html)
       
        
        
        data="website create of the url -: "+url  
        conn.send(data.encode(FORMAT)) #sending msg back to client 

    conn.close() #closing the connection

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #sock stream reffeed ecp protocal which is connection oriented protocal
    server.bind(ADDR)#bind function take ip and port in a tuple
    server.listen() #listen to client
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:  #infinte loop till we stop the program
        conn, addr = server.accept()   #loop wait for client to connect
        thread = threading.Thread(target=handle_client, args=(conn, addr))  #creating a thread to handle client,conn helps to recive and send request
        thread.start() #start the thread
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #minus the main 

if __name__ == "__main__":
    main()      #define main sever