import socket

IP = "127.0.0.1"
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
while True:
    expression = input("Введите математическое выражение (например, 2+2) или 'history' для истории: ")
    client.send(expression.encode())

    response = client.recv(1024).decode()

    if "Ошибка" in response:
        print(f"Ошибка: {response}")
    else:
        print(f"Ответ сервера:\n{response}")
    if expression.lower() == "exit":
        break
client.close()