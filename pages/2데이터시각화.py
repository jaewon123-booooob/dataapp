# -*- coding:utf-8 -*-
import pandas as pd

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="graph", page_icon="🎉")
st.sidebar.header("데이터 시각화")



st.markdown("## 시각화 개요 \n"
"본 프로젝트는     를 알려주는 대시보드입니다. "
"여기에 추가 내용을 더 넣을 수 있습니다.")


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### 연관성 파악을 위한 시각화 ")

df = pd.read_csv('Thyroid_Diff.csv')

dh=df.head()
st.write(dh)

tab1, tab2, tab3= st.tabs(["나이", "흡연 상태", "병기와 치료계수"])

with tab1: #total bill
    fig, ax = plt.subplots()
    st.header("나이-분포 히스토그램")
    fig = plt.figure(figsize=(10, 5))
    sns.histplot(x='Age', data=df, hue='Gender', kde=True, palette='coolwarm', edgecolor='black')
    plt.title("Age Distribution by Gender")
    plt.xlabel("Age")
    plt.ylabel("Count")
    st.pyplot(fig)

with tab2:
    st.header("흡연 상태에 따른 병지학적 결과 Boxplot")
    fig = plt.figure(figsize=(10, 5))
    sns.boxplot(x='Smoking', y='Pathology', data=df, palette='pastel')
    plt.title("Pathology by Smoking Status")
    plt.xlabel("Smoking Status")
    plt.ylabel("Pathology Score")
    st.pyplot(fig)


with tab3:
    st.header("병기와 치료반응 Scatterplot")
    fig = plt.figure(figsize=(10, 5))
    sns.scatterplot(x='Stage', y='Response', data=df, hue='Risk', style='Gender', palette='viridis')
    plt.title("Stage vs Response with Risk and Gender")
    plt.xlabel("Stage")
    plt.ylabel("Response")
    st.pyplot(fig)
