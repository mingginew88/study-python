import streamlit as st
from cryptocmd import CmcScraper
import plotly.express as px

st.write('# 비트코인 BTC 데이터')

scrppper = CmcScraper('BTC', '01-01-2021', '07-01-2021') # %d-%m-%Y

df = scrppper.get_dataframe()

fig_close = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'], title='가격')
fig_volume = px.line(df, x='Date', y=['Volume'], title='거래량')

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)