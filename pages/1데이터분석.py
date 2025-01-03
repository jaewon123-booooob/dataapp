import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write("# Thyroid 갑상선 데이터 웹앱 🌸")

st.header("갑상선 데이터 개요 ",divider='rainbow')


df = pd.read_csv('평가/data/Thyroid_Diff.csv')
st.markdown('''
             
    Thyroid.csv 데이터를 참조해 갑상선 데이터를 분석해보자. \n
    
    환자의 나이, 성별, 흡연 이력 등 다양한 데이터를 포함하며, 연속형 특성, 범주형 특성, 분류대상의 포인트가 있습니다.
    이 데이터를 통해 환자 특성과 질환의 재발 여부 간의 관계를 분석하고 특성 특징이 재발 가능성에 미치는 영향을 파악합니다.
    ''' )

col1, col2, col3=st.columns([4,4,4])
with col1:
    st.header('col1')
    st.image('갑상선.jpg')
with col2:
    st.header('col2')
    st.image('림프절.jpg')
with col3:
    st.header('col3')
    st.image('갑상선암.jpg')


tab1,tab2=st.tabs(['🌸 데이터 분석','🌸 데이터 시각화'])


with tab1:
    st.header('데이터 분석')
    st.markdown(""" 
        - Age(나이)
        - Gender (성별)
        - Smoking (현재 흡연 여부)
        - Hx Smoking (흡연 이력 여부)
        - Hx Radiothreapy (방사선 치료 이력 여부)
        - Thyroid Function (갑상선 기능 상태)
        - Physical Examination (신체 검사 결과)
        - Adenopathy (림프절 비대 여부)
        - Pathology (병리학적 결과)
        - Focality (병변의 초점 수)
        - Risk (위험도 평가)
        - T, N, M (TNM 병기 분류)
        - Stage (종합적인 병기 단계)
        - Response (치료에 대한 반응 상태)
                  """)





    st.subheader('데이터 파악')
    st.write(df.head(10))

    st.subheader('데이터 통계')
    st.dataframe(df.describe(include='all'))
    
    st.subheader('데이터 추출')
    col = st.multiselect('select column',df.columns)
    new_df = df.loc[:,col]
    st.write(new_df)

with tab2:
    st.header('데이터 시각화')


    st.subheader("나이 분포 히스토그램")
    fig = plt.figure(figsize=(10, 5))
    sns.histplot(x='Age', data=df, hue='Gender', kde=True, palette='coolwarm', edgecolor='black')
    plt.title("Age Distribution by Gender")
    plt.xlabel("Age")
    plt.ylabel("Count")
    st.pyplot(fig)


    st.subheader("흡연 상태에 따른 병리학적 결과 Boxplot")
    fig = plt.figure(figsize=(10, 5))
    sns.boxplot(x='Smoking', y='Pathology', data=df, palette='pastel')
    plt.title("Pathology by Smoking Status")
    plt.xlabel("Smoking Status")
    plt.ylabel("Pathology Score")
    st.pyplot(fig)


    st.subheader("병기(Stage)와 치료 반응(Response) Scatterplot")
    fig = plt.figure(figsize=(10, 5))
    sns.scatterplot(x='Stage', y='Response', data=df, hue='Risk', style='Gender', palette='viridis')
    plt.title("Stage vs Response with Risk and Gender")
    plt.xlabel("Stage")
    plt.ylabel("Response")
    st.pyplot(fig)
