import socket

def client_bai3():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12347))

    numbers = input("Nhập chuỗi số nguyên cách nhau bằng dấu cách: ").strip()
    client.send(numbers.encode())

    response = client.recv(1024).decode()
    print(f"Kết quả từ server: {response}")

    client.close()

client_bai3()
