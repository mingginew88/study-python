import pandas as pd
from faker import Faker

######################################################
# 조건
row = 100       # 생성할 row 수
# 생성 언어 (lang = '', default : English)
lang = 'ko_KR'
faker = Faker(lang)

# 칼럼명 리스트 와 사용할 함수 리스트 갯수 일치
# 칼럼명 리스트
column_name_list = ['이름', '주소', '전화번호', '날짜', '하고 싶은 말']
# 사용할 함수 리스트
use_func_list = [faker.name, faker.address, faker.phone_number, faker.date, faker.word]
# faker.name()                      # 이름
# faker.phone_number()              # 전화번호
# faker.job()                       # 직업
# faker.date(pattern='%Y-%m-%d')    # 날짜
# faker.address()                   # 주소
# faker.ipv4_private()              # IP
# faker.word()                      # 문장
# faker.profile()                   # 유저정보
######################################################

df = pd.DataFrame()

## 커스텀 샘플 데이터 생성
def custom_sample():
    global df
    df = pd.DataFrame()
    for idx, val in enumerate(column_name_list):
        temp_list = []

        for i in range(row):
            temp_list.append(use_func_list[idx]())

        df_temp = pd.DataFrame(temp_list, columns=[val])
        df = pd.concat([df, df_temp], axis=1)


## 가상 유저정보 생성
def sample_profile():
    global df
    df = pd.DataFrame()
    temp_list = []

    for i in range(row):
        temp_list.append(faker.profile())

    df_temp = pd.DataFrame(temp_list)
    df = pd.concat([df, df_temp], axis=1)

## CSV 생성
def createCSV():
    df.to_csv('./files/sampleData.csv', index=False, encoding='utf-8')

custom_sample()
# sample_profile()
createCSV()
