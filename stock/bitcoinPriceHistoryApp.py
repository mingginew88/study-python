import streamlit as st
from cryptocmd import CmcScraper
import plotly.express as px
from datetime import datetime

st.write('#Cryptocurrency Web App')
st.sidebar.header('Menu')

name = st.sidebar.selectbox('Name', ['BTC', 'ETH', 'USDT'])

start_date = st.sidebar.date_input('start date', datetime(2021, 1, 1))
end_date = st.sidebar.date_input('end date', datetime(2021, 1, 25))

scrapper = CmcScraper(name, start_date.strftime('%d-%m-%Y'), end_date.strftime('%d-%m-%Y'))

df = scrapper.get_dataframe()

fig_close = px.line(df, x='Date', y=['Open', 'High', 'Low', 'Close'], title='Price')
fig_volume = px.line(df, x='Date', y=['Volume'], title='Volume')

st.plotly_chart(fig_close)
st.plotly_chart(fig_volume)
