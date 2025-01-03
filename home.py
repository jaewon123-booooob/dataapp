import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='Home', page_icon='👀')


df=pd.read_csv("iris.csv")
st.write(df.head())
fig=plt.figure(figsize=(12,4)) #그래프 사이즈 가로, 세로
sns.lineplot(data=df, x='SepalLength', y='SepalWidth') #그래프 그리기



ck=st.checkbox('show graph')
if ck:
    st.pyplot(fig) # 웹 그래프 보여주기

st.sidebar.title('sidebar area')
se=st.sidebar.selectbox('text select..', ('a','b'))
st.write('select', se)

rd=st.sidebar.radio('select radio', ('SepalLength', 'SepalWidth'))
st.dataframe(df[rd])

col1, col2=st.columns([8,4])
with col1:
    st.header('col1')
    st.image('cat.jpg')
with col2:
    st.header('col2')
    st.image('cat.jpg')

t1, t2=st.tabs(['❤ t1 label', '😍 t2 label']) #윈도우+마침표 = 이모티콘
with t1:
    st.header('tab1 area')

with t2:
    st.header('tab2 area')