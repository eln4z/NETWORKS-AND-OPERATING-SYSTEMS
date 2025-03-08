import socket
import datetime
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))
# message = input("Enter message: ")
start_time =datetime.datetime.now()
# client_socket.sendall(message.encode())
# response = client_socket.recv(1024)
# print(f"Server response: {response.decode()}")
end_time = datetime.datetime.now()
with open('file_to_send.txt', 'rb') as f:
    client_socket.sendfile(f)
    client_socket.close()

diff_time =(end_time - start_time).total_seconds()
print(f"Time TCP took in seconds {diff_time}")