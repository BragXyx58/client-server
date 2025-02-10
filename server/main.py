import socket

IP = "127.0.0.1"
PORT = 4000


def calculate(expression):
    for op in ('+', '-', '*', '/'):
        if op in expression:
            left, right = expression.split(op)
            left, right = left.strip(), right.strip()

            if op == '/' and right == '0':
                return "Ошибка: Деление на ноль!"

            return str(eval(left + op + right))

    return "Ошибка: Некорректное выражение"



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)
print("Сервер запущен, ожидание подключения...")

conn, addr = server.accept()
print(f"Подключение от: {addr}")

data = conn.recv(1024).decode()
print(f"Получено выражение: {data}")

result = calculate(data)
conn.send(result.encode())

conn.close()
server.close()