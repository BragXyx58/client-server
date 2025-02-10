import socket
IP = "127.0.0.1"
PORT = 4000
HISTORY_FILE = "history.txt"

def save_to_history(expression, result):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"{expression} = {result}\n")

def get_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return file.read().strip() or "История пуста"
    except FileNotFoundError:
        return "История пуста"

def calculate(expression):
    for op in ('+', '-', '*', '/'):
        if op in expression:
            left, right = expression.split(op)
            left, right = left.strip(), right.strip()

            if op == '/' and right == '0':
                return "Ошибка: Деление на ноль!"

            result = str(eval(left + op + right))
            save_to_history(expression, result)
            return result

        return "Ошибка: Некорректное выражение"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)
print("Сервер запущен, ожидание подключения...")

while True:
    conn, addr = server.accept()
    print(f"Подключение от: {addr}")

    data = conn.recv(1024).decode().strip()
    print(f"Получено сообщение: {data}")

    if data.lower() == "history":
        result = get_history()
    else:
        result = calculate(data)

    conn.send(result.encode())
    conn.close()
