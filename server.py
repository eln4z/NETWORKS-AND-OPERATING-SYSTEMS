import socket
# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))
server_socket.listen(1) # Allow 1 pending connection
print("TCP Server is listening...")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")
    
    # ... (Server setup code)
    with open('received_file.txt', 'wb') as f:
        #while True:
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
    # Echo back the data
        client_socket.sendall(b"ACK: " + data)        
        if not data:
            print("not data!")
            break
        f.write(data)
        print("text recorded!")
    client_socket.close()