https://www.youtube.com/watch?v=aYwg1H5BK04 참고

# 파이썬 웹 크롤링

### 1. 웹크롤링이란? 웹사이트를 접속하는 행위, HTML데이터를 가져오고 parsing까지 하는 행위
대상 http://news.naver.com
수시로 바뀌는 데이터 값을 긁어오는 것은 크롤러가 유용.

### 2. beautifulsoup 설치
https://www.youtube.com/redirect?event=comments&redir_token=QUFFLUhqbWhVTi1VRWNBV1FXR1Btelh6aTdjcmVaTXoxd3xBQ3Jtc0tuMEMyek1FbmxxQW1MblJ0Sldtb2JxYU9rVFkxWXZtTDZPMC1ONmtUTFItU0lrYWl4Q0NkYTFETEtnRUtaR2VrWGFZd0FvY2tGNmJ0LXBBeTY5VmVJYi1GNkpyN1JpcUJlTlhFYS1QNS0zOXBod00zRQ&q=https%3A%2F%2Fstudyhard24.tistory.com%2F235&stzid=UgzrHliJh5jONdzCFbB4AaABAg.9GtfmqQv_4C9H0fRRS9TmT
<a href="https://ibb.co/2SNSV4z"><img src="https://i.ibb.co/ypSpvjz/beautiful-Soup-bs4.jpg" alt="python_img" border="0"></a>

### 3. 코드
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://news.naver.com/")

bsObject = BeautifulSoup(html, "html.parser")

for link in bsObject.find_all('a'):                  # << 하이퍼링크 가져오기
    print(link.text.strip(), link.get('href'))

for link in bsObject.find_all('img'):               # << 이미지링크 가져오기 
    print(link.text.strip(), link.get('src'))
