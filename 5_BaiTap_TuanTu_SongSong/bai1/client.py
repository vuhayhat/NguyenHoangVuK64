import socket

def client_bai1():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    numbers = input("Nhập hai số nguyên (a, b): ")
    client.send(numbers.encode())
    response = client.recv(1024).decode()
    print(f"Kết quả từ server: {response}")
    client.close()

client_bai1()
