import socket
from threading import Thread

def handle_client(conn, addr):
    print(f"Kết nối từ {addr}")
    data = conn.recv(1024).decode()  # Nhận dữ liệu từ client
    try:
        # Tách và chuyển dữ liệu thành hai số nguyên a và b
        a, b = map(int, data.split())

        # Kiểm tra nếu a lớn hơn b
        if a > b:
            conn.send(b"a  nho hon hoac bang b.".encode())
        else:
            # Tìm các số trong khoảng a -> b có tổng chữ số bằng 5
            result = ' '.join(str(i) for i in range(a, b + 1) if sum(map(int, str(i))) == 5)

            # Nếu không có số nào thỏa mãn
            if result:
                conn.send(result.encode())
            else:
                conn.send(b"khong co so nao co tong chu so bang 5.")

    except ValueError:
        # Trả về thông báo lỗi nếu dữ liệu không hợp lệ
        conn.send(b"loi nhap dung 2 so nguyen")

    finally:
        conn.close()  # Đóng kết nối sau khi xử lý

def server_bai2():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12346))  # Ràng buộc địa chỉ và cổng
    server.listen(5)  # Lắng nghe tối đa 5 kết nối chờ
    print("Server đang chạy (Bài 2)...")

    while True:
        conn, addr = server.accept()  # Chấp nhận kết nối từ client
        Thread(target=handle_client, args=(conn, addr)).start()  # Xử lý mỗi client trong 1 thread

# Khởi chạy server
server_bai2()
