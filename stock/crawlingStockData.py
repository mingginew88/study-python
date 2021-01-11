import requests
import pandas as pd
from bs4 import BeautifulSoup
import openpyxl
from datetime import datetime

## 크롤링 할 페이지
req = requests.get('https://finance.naver.com/sise/sise_market_sum.nhn?&page=1')

## HTML 코드 저장
html = req.text

## BeautifulSoup으로 html소스를 python 객체로 변환
## 첫 인자 : html소스코드
## 두 번째 인자 : parser 종류 명시
## Python 내장 html.parser를 이용
soup = BeautifulSoup(html, 'html.parser')

## 데이터 가공을 위한 dataframe 활용
contents = soup.find_all(attrs={'class': 'type_2'})
dfContent = []
allDfContents = []

for content in contents:
    trs = content.find_all("tr")
    for tr in trs:
        ths = tr.find_all("th")
        for th in ths:
            dfContent.append(th.text)
        if dfContent:
            allDfContents.append(dfContent)
            dfContent = []

        tds = tr.find_all("td")
        for td in tds:
            dfContent.append(td.text)
        if dfContent:
            allDfContents.append(dfContent)
            dfContent = []

## pandas를 이용한 dataframe 생성
dfContents = pd.DataFrame(allDfContents)
## 공백 제거 : None 값 제거
dfContents = dfContents[dfContents[1].notnull()]
## 엑셀에 데이터 저장
excelPath = 'D:/study/study-python/stock/stockData_' + str(datetime.today().strftime("%Y%m%d")) + '.xlsx'
dfContents.to_excel(excel_writer=excelPath)

print('End')