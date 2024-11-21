import socket
import qrcode
from PIL import Image
import io

def generate_qrcode(data):
    """Tạo mã QR từ dữ liệu đầu vào."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def serve_client(client_socket):
    """Xử lý kết nối từ Client."""
    try:
        data = client_socket.recv(1024).decode()
        print(f"Nhận dữ liệu từ Client: {data}")

        # Tạo mã QR
        qr_img = generate_qrcode(data)

        # Chuyển đổi hình ảnh thành byte
        img_byte_arr = io.BytesIO()
        qr_img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Gửi kích thước của hình ảnh
        client_socket.send(str(len(img_byte_arr)).encode())
        client_socket.recv(1024)  # Chờ Client xác nhận

        # Gửi hình ảnh
        client_socket.sendall(img_byte_arr)
        print("Đã gửi mã QR đến Client.")

    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        client_socket.close()

def start_server():
    """Khởi động Server."""
    host = '127.0.0.1'  # Địa chỉ IP của Server
    port = 65432        # Cổng kết nối

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server đang lắng nghe trên {host}:{port}")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Kết nối từ {addr}")
            serve_client(client_socket)

if __name__ == "__main__":
    start_server()