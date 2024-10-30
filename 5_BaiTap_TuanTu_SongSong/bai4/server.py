import socket
from threading import Thread

def handle_client(conn, addr):
    print(f"Kết nối từ {addr}")
    data = conn.recv(1024).decode()
    try:
        max_number = max(map(int, data.split()))
        conn.send(str(max_number).encode())
    except ValueError:
        conn.send(b"Loi nhap chuoi so nguyen kh hop le.")
    finally:
        conn.close()

def server_bai4():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12348))
    server.listen(5)
    print("Server đang chạy (Bài 4)...")

    while True:
        conn, addr = server.accept()
        Thread(target=handle_client, args=(conn, addr)).start()

server_bai4()
