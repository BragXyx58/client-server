import socket

IP = "127.0.0.1"
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

expression = input("Введите математическое выражение (например, 2+2): ")
client.send(expression.encode())

response = client.recv(1024).decode()
print(f"Результат: {response}")

client.close()