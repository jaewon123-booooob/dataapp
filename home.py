import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='Home', page_icon='👀')


st.write("# Thyroid 갑상선 데이터 웹앱 🌸")

st.header("갑상선 데이터 개요 ",divider='rainbow')


df = pd.read_csv('Thyroid_Diff.csv')
st.markdown('''
             
    Thyroid.csv 데이터를 참조해 갑상선 데이터를 분석해보자. \n
    
    환자의 나이, 성별, 흡연 이력 등 다양한 데이터를 포함하며, 연속형 특성, 범주형 특성, 분류대상의 포인트가 있습니다.
    이 데이터를 통해 환자 특성과 질환의 재발 여부 간의 관계를 분석하고 특성 특징이 재발 가능성에 미치는 영향을 파악합니다.
    ''' )


