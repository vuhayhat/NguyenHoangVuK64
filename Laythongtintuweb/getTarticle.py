
import requests
from bs4 import BeautifulSoup

response = requests.get('https://vnexpress.net')

if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    article_tag = soup.find('article')


    if article_tag:
        article_content = article_tag.get_text(strip=True)
        with open('article_content.txt', 'w', encoding='utf-8') as file: 
            file.write(article_content)     
    else:
        print("No <article> tag found.")   
else:
    print(f"lấy nội dung thất bại , trạng thái : {response.status_code}")