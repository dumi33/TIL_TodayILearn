import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml") # 객체 생성 

 
images = soup.find_all("img", attrs = {"class" : "thumb_img"})

for idx, image in enumerate(images) :
    image_res = requests.get(image["src"]) 
    image_res.raise_for_status() # 문제가 있을 경우 
    
    with open("movie{}.jpg".format(idx+1), "wb") as f :
        f.write(image_res.content)

    if idx >=4 :  # 상위 5개 파일만 저장 
        break
