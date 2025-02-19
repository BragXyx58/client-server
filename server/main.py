import socket

IP = "127.0.0.1"
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(2)

print("Сервер запущен, ожидаю подключения первого клиента...")
conn1, addr1 = server.accept()
print(f"Первый клиент подключился: {addr1}")

msg = conn1.recv(1024).decode()
if not msg:
    print("Ошибка: не получено сообщение от первого клиента")
else:
    print(f"Получено сообщение от первого клиента: {msg}")

print("Ожидаю подключения второго клиента...")
conn2, addr2 = server.accept()
print(f"Второй клиент подключился: {addr2}")

if msg:
    conn2.sendall(msg.encode())
    print("Сообщение отправлено второму клиенту")

conn1.close()
conn2.close()
server.close()
print("Сервер завершил работу")
