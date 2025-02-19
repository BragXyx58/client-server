import socket

IP = "127.0.0.1"
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
print("Подключен к серверу")

message = client.recv(1024).decode()
print("Сообщение от первого клиента:", message)

client.close()
print("Второй клиент завершил работу")
