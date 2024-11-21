import socket
import cv2
import numpy as np

def receive_qrcode(client_socket):
    """Nhận mã QR từ Server."""
    try:
        # Nhận kích thước của hình ảnh
        img_size = int(client_socket.recv(1024).decode())
        client_socket.send("ACK".encode())  # Gửi xác nhận

        # Nhận hình ảnh
        img_bytes = b''
        while len(img_bytes) < img_size:
            chunk = client_socket.recv(4096)
            if not chunk:
                break
            img_bytes += chunk

        # Chuyển đổi byte thành hình ảnh
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img

    except Exception as e:
        print(f"Lỗi: {e}")
        return None

def start_client():
    """Khởi động Client."""
    host = '127.0.0.1'  # Địa chỉ IP của Server
    port = 65432        # Cổng kết nối

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # Nhập dữ liệu từ người dùng
        data = input("Nhập văn bản hoặc URL: ")
        client_socket.send(data.encode())

        # Nhận và hiển thị mã QR
        qr_img = receive_qrcode(client_socket)
        if qr_img is not None:
            cv2.imshow('Mã QR', qr_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == "__main__":
    start_client()