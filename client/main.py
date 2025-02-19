import socket

IP = "127.0.0.1"
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
print("Подключен к серверу")

message = input("Введите сообщение для второго клиента: ")
client.sendall(message.encode())
print("Сообщение отправлено серверу")

client.close()
print("Первый клиент завершил работу")
