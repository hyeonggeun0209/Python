import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://naver.com/")
soup = bs(page.text, "html.parser")

elements = soup.select('div.info_box > strong')

for index, element in enumerate(elements, 1):
		print("{} 번째 게시글의 제목: {}".format(index, element.text))