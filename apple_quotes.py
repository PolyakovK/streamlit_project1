import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

# Заголовок для приложения
st.title('Котировки акций Apple')

# Установка начальных и конечных дат для слайдеров
start_date = st.sidebar.date_input('Дата начала', datetime(2022, 1, 1))
end_date = st.sidebar.date_input('Дата конца', datetime(2023, 1, 1))

# Проверка корректности выбранного диапазона дат
if start_date >= end_date:
    st.error('Ошибка: Дата начала должна быть раньше даты конца.')
else:
    # Получение данных акций Apple
    ticker = 'AAPL'
    data = yf.download(ticker, start=start_date, end=end_date)

    # Создание графика японских свечей с использованием Plotly
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])

    # Настройка заголовков и осей
    fig.update_layout(title=f'Котировки акций {ticker} в виде японских свечей',
                      xaxis_title='Дата',
                      yaxis_title='Цена')

    # Отображение графика в Streamlit
    st.plotly_chart(fig)