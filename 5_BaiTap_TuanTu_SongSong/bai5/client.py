import socket

def client_bai5():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12349))

    number = input("Nhập 1 số nguyên: ").strip()
    client.send(number.encode())

    response = client.recv(1024).decode()
    print(f"Kết quả từ server: {response}")

    client.close()

client_bai5()
