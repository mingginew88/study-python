import streamlit as st
import pandas_datareader as pdr
from datetime import datetime

# 실행 방법
# streamlit run 파일명.py

## 문구 작성
st.write('''
# 삼성전자 주식 데이터
마감 가격과 거래량 차트
''')

start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# yahoo 데이터
# df = pdr.get_data_yahoo('005930.KS', start_date, end_date)

# yahoo, google 등 직접 사이트 경로 입력
df = pdr.DataReader('005930.KS', 'yahoo', start_date, end_date)

# streamlit 을 활용한 마감가격과 거래량 그리기기
st.line_chart(df.Close)     # 마감가격
st.line_chart(df.Volume)    # 거래량



