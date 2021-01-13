from selenium import webdriver
from selenium.webdriver.support.select import Select

## 개인 계정정보
ID = '계정명'
PW = '계정비밀번호'

## 크롬 드라이버를 이용(Win32)
## 사용시 크롬 인터넷 버전에 맞게 드라이버 다운로드
driver = webdriver.Chrome()

## 로또 접속 페이지 이동
URL = 'https://dhlottery.co.kr/user.do?method=login&returnUrl='
driver.get(URL)

## 아이디 입력
elem_login = driver.find_element_by_id('userId')
elem_login.send_keys(ID)

## 비밀번호 입력
elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys(PW)

## 로그인 버튼 클릭
## Xpath 경로는 개발자도구의 요소값 우클릭하여 Copy - Copy Xpath
LOGIN_XPATH = '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a'
driver.find_element_by_xpath(LOGIN_XPATH).click()

## 로또 구매창 이동
driver.get('https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40')

## 자동 구매 버튼 클릭
driver.switch_to.frame('ifrm_tab')
driver.find_element_by_xpath('//*[@id="num2"]/span').click()

## 로또 구매 개수 선택
select = Select(driver.find_element_by_xpath('//*[@id="amoundApply"]'))
select.select_by_value('2')

## 로또 구매 확인 버튼 클릭
driver.find_element_by_xpath('//*[@id="btnSelectNum"]').click()

## 구매 확인 버튼 클릭
driver.find_element_by_xpath('//*[@id="btnBuy"]').click()

## 확인버튼
alert = driver.switch_to.alert
alert.accept()

## 크롬종료
driver.close()