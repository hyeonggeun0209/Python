import time, random, re
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

page = requests.get("https://www.juso.go.kr/support/AddressMainSearch.do?searchKeyword=%EA%B3%A0%EC%96%91%EC%8B%9C+%EC%95%84%ED%8C%8C%ED%8A%B8&dsgubuntext=&dscity1text=&dscounty1text=&dsemd1text=&dsri1text=&dssan1text=&dsrd_nm1text=&aotYn=N")
soup = bs(page.text, "html.parser")

elements = soup.select('div.container.support_search_list > div.search_list > ol > li')

for index, element in enumerate(elements, 1):
    print("{} 번째 주소: {}".format(index, element.text))

