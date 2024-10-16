import socket
def start_server():
    host = '127.0.0.1'
    port = 60000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                try:
                    num1, num2 = map(float, data.split(","))
                    result = num1 + num2
                    response = f" {num1} + {num2} = {result}"
                except ValueError:
                    response = "Nhập không hợp lệ vui lòng Nhập số thứ nhất rồi nhấn enter sau đó nhập số thứ 2"
                conn.sendall(response.encode())
if __name__ =="__main__":
    start_server()
