import requests
from bs4 import BeautifulSoup

# Gửi yêu cầu HTTP đến trang web
response = requests.get('https://www.didongmy.com/40-anh-meme-vui-nho-n-va-ha-i-huo-c-nhat-2024')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Tìm tất cả các thẻ img
    for i, img in enumerate(soup.find_all('img')):
        src = img.get('src')
        if src:
            # Đảm bảo đường dẫn ảnh đầy đủ
            if src.startswith('/'):
                src = 'https:' + src

            # Tải và lưu ảnh
            img_data = requests.get(src).content
            with open(f'image_{i+1}.jpg', 'wb') as file:
                file.write(img_data)
            print(f"Đã lưu ảnh: image_{i+1}.jpg")
else:
    print(f"Thất bại, trạng thái code: {response.status_code}")
