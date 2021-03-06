import streamlit as st
import pandas as pd
import plotly.express as px

st.session_state['answer'] = ''

st.write(st.session_state)

realans = ['', 'abc', 'edf']

if  st.session_state['answer'] in realans:
    answerStat = "correct"
elif st.session_state['answer'] not in realans:
    answerStat = "incorrect"

st.write(st.session_state)
st.write(answerStat)

@st.cache()
def load_data():
    df = pd.read_excel('https://www.cbr.ru/Queries/UniDbQuery/DownloadExcel/14315?Posted=True&From=01.01.2019&To=26.11.2021&FromDate=01%2F01%2F2019&ToDate=11%2F26%2F2021', 0, header=0, index_col=None, na_values=["NA"])
    return df

df = load_data()

df['month'] = pd.DatetimeIndex(df['DT']).month
df['year'] = pd.DatetimeIndex(df['DT']).year
#df['vol'] = df['vol'].dropna
#display(df)

fig = px.histogram(df, x="vol", y="ruo", color="year",
                   marginal="box", # or violin, rug
                   hover_data=df.columns)

st.plotly_chart(fig)