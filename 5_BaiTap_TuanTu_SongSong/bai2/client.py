import socket

def client_bai2():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12346))  # Kết nối tới server

    # Nhập dữ liệu từ người dùng
    numbers = input("Nhập hai số nguyên (a b): ").strip()

    # Gửi dữ liệu tới server
    client.send(numbers.encode())

    # Nhận phản hồi từ server
    response = client.recv(1024).decode()
    print(f"Kết quả từ server: {response}")

    client.close()  # Đóng kết nối

# Khởi chạy client
client_bai2()
