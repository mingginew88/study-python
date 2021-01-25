import streamlit as st
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

# 실행 방법
# streamlit run 파일명.py

# 기업정보 DataFrame 함수
def get_company_info():
    df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
    df = df[['회사명', '종목코드']]
    df = df.rename(columns={'회사명': 'name', '종목코드': 'code'})
    df.code = df.code.map('{:06d}'.format)

    return df

# 코드번호 추출 함수
def get_code_no(df, name):
    code = df.query("name=='{}'".format(name))['code'].to_string(index=False)
    code = code.strip() + '.KS'
    print(code)
    return code

## 문구 작성
st.write('''
# 주식 데이터
마감 가격과 거래량 차트
''')

st.sidebar.header('Menu')

# 기업 정보 가져오기
df = get_company_info()

# 회사명 추출
test_list = df['name']

# 기업명 Select Box
name = st.sidebar.selectbox('Name', test_list)

# 기업 코드번호 추출
code = get_code_no(df, name)

start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# yahoo 데이터
df_result = pdr.get_data_yahoo(str(code), start_date, end_date)

# yahoo, google 등 직접 사이트 경로 입력
# df_result = pdr.DataReader(str(code), 'yahoo', start_date, end_date)

# streamlit 을 활용한 마감가격과 거래량 그리기기
st.line_chart(df_result.Close)     # 마감가격
st.line_chart(df_result.Volume)    # 거래량



