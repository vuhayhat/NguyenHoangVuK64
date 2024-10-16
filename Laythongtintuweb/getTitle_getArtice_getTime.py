import requests
from bs4 import BeautifulSoup

response = requests.get('https://vietnamnet.vn/thu-tuong-khong-de-nguoi-dan-o-lai-cac-khu-vuc-nguy-hiem-khi-lu-len-cao-2321132.html')

if response.status_code == 200:
    
    soup = BeautifulSoup(response.content,'html.parser')
    title = soup.find(class_= "content-detail-title").get_text(strip=True)
    article_tag = soup.find(class_="maincontent main-content")
    article_date = soup.find(class_= "bread-crumb-detail__time")
    
    if article_date:
        date = article_date.get_text(strip=True)
    if article_tag:
        article_content = article_tag.get_text(strip=True)
        with open('article_content.txt', 'w', encoding='utf-8') as file: 
            file.write(title +"\n")
            file.write(date +"\n")
            file.write(article_content)
    else:
        print("No <article> tag found.")
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")