import socket
from threading import Thread

def handle_client(conn, addr):
    print(f"Kết nối từ {addr}")
    data = conn.recv(1024).decode()
    try:
        sorted_numbers = ' '.join(sorted(data.split(), key=int))
        conn.send(sorted_numbers.encode())
    except ValueError:
        conn.send(b"Loi : nhap toan so nguyen hop le")
    finally:
        conn.close()

def server_bai3():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12347))
    server.listen(5)
    print("Server đang chạy (Bài 3)...")

    while True:
        conn, addr = server.accept()
        Thread(target=handle_client, args=(conn, addr)).start()

server_bai3()
