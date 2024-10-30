import socket
from threading import Thread

def handle_client(conn, addr):
    print(f"Kết nối từ {addr}")
    data = conn.recv(1024).decode()
    a, b = map(int, data.split())
    result = ' '.join(str(i) for i in range(a, b + 1))
    conn.send(result.encode())
    conn.close()

def server_bai1(protocol='TCP', mode='sequential'):
    if protocol == 'TCP':
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 12345))
        server.listen(5)
        print("Server đang chạy (Bài 1)...")
        while True:
            conn, addr = server.accept()
            if mode == 'parallel':
                Thread(target=handle_client, args=(conn, addr)).start()
            else:
                handle_client(conn, addr)
    else:
        print("Giao thức UDP không hỗ trợ cho bài 1")

server_bai1(protocol='TCP', mode='sequential')
