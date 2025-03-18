import socket

# Create a UDP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))

print("UDP Server is ready to receive weather data...")

while True:
    data, client_address = server_socket.recvfrom(2048)  # Receive data from client
    print(f"Received weather data from {client_address}: {data.decode()}")
