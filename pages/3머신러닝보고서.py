import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="machine", page_icon="🎉")
st.sidebar.header("머신러닝 보고서")



df = pd.read_csv('Thyroid_Diff.csv')
st.header("갑상선 머신러닝 보고서")
st.subheader('데이터보기')
st.write(df)



# Séparation des caractéristiques (X) et de la cible (y)
X = df.drop(columns=['Recurred'])  # Features
y = df['Recurred']  # Target variable


# Encodage des variables catégorielles
label_encoder = LabelEncoder()
X['Gender'] = label_encoder.fit_transform(X['Gender'])
X['Smoking'] = label_encoder.fit_transform(X['Smoking'])
X['Hx Smoking'] = label_encoder.fit_transform(X['Hx Smoking'])
X['Hx Radiothreapy'] = label_encoder.fit_transform(X['Hx Radiothreapy'])
X['Thyroid Function'] = label_encoder.fit_transform(X['Thyroid Function'])
X['Physical Examination'] = label_encoder.fit_transform(X['Physical Examination'])
X['Adenopathy'] = label_encoder.fit_transform(X['Adenopathy'])
X['Pathology'] = label_encoder.fit_transform(X['Pathology'])
X['Focality'] = label_encoder.fit_transform(X['Focality'])
X['Risk'] = label_encoder.fit_transform(X['Risk'])
X['T'] = label_encoder.fit_transform(X['T'])
X['N'] = label_encoder.fit_transform(X['N'])
X['M'] = label_encoder.fit_transform(X['M'])
X['Stage'] = label_encoder.fit_transform(X['Stage'])
X['Response'] = label_encoder.fit_transform(X['Response'])


# 데이터시각화 - Age distribution

fig=plt.figure(figsize = (8, 6))
sns.histplot(df['Age'], bins = 20, kde = True, color = 'skyblue', edgecolor = 'black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
st.pyplot(fig)






#split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Normalisation des caractéristiques numériques
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Construction du modèle de prédiction (Random Forest Classifier)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluation du modèle
accuracy = accuracy_score(y_test, y_pred)
st.write(f'Accuracy: {accuracy:.2f}')

# Rapport de classification
st.write(classification_report(y_test, y_pred))

# Matrice de confusion
conf_matrix = confusion_matrix(y_test, y_pred)
fig=plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap="YlGnBu", fmt='d', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')

st.pyplot(fig)
