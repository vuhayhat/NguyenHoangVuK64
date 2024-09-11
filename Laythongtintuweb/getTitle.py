import requests
from bs4 import BeautifulSoup

response = requests.get('https://vnexpress.net')

if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    title = soup.title.string

    print("Tiêu đề của trang:", title)
else:
    print(f"thất bại, không thể lấy tiêu đề : {response.status_code}")