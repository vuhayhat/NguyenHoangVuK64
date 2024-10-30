import socket
from threading import Thread

def handle_client(conn, addr):
    print(f"Kết nối từ {addr}")
    data = conn.recv(1024).decode()
    try:
        digit_sum = sum(map(int, data))
        conn.send(str(digit_sum).encode())
    except ValueError:
        conn.send(b"nhap so kh hop le")
    finally:
        conn.close()

def server_bai5():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12349))
    server.listen(5)
    print("Server đang chạy (Bài 5)...")

    while True:
        conn, addr = server.accept()
        Thread(target=handle_client, args=(conn, addr)).start()

server_bai5()
