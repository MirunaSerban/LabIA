import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder


# Exercitiul 1
df = pd.read_csv('StudentsPerformance.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())


# Exercitiul 2
variabile_categorice = df.select_dtypes(include=['object']).columns.tolist()
variabile_numerice = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

print(f"Variabile categorice: {variabile_categorice}")
print(f"Variabile numerice: {variabile_numerice}")


# Exercitiul 3
for col in variabile_numerice:
    df[col] = df[col].fillna(df[col].median())

for col in variabile_categorice:
    df[col] = df[col].fillna('Unknown')

print(df.isnull().sum())


# Exercitiul 4
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])

df = pd.get_dummies(df, columns=['race/ethnicity', 'parental level of education', 'lunch', 'test preparation course'])

print(df.head())


# Exercitiul 5
df['average_score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3

def categorie_performanta(scor):
    if scor < 50:
        return 'low'
    elif scor <= 70:
        return 'medium'
    else:
        return 'high'

df['performance_level'] = df['average_score'].apply(categorie_performanta)

df['is_prepared'] = df['test preparation course_completed'].astype(int)

print(df[['average_score', 'performance_level', 'is_prepared']].head(10))


# Exercitiul 6
coloane_corelate = df.select_dtypes(include=[np.number]).corr()
print(coloane_corelate)

coloane_constante = [col for col in df.columns if df[col].nunique() == 1]
print(f"Coloane constante: {coloane_constante}")

for col in coloane_constante:
    df = df.drop(columns=[col])


# Exercitiul 7
scaler = StandardScaler()
coloane_de_scalat = ['math score', 'reading score', 'writing score', 'average_score']

print("Inainte de scalare:")
print(df[coloane_de_scalat].head())

df_scalat = df.copy()
df_scalat[coloane_de_scalat] = scaler.fit_transform(df[coloane_de_scalat])

print("Dupa scalare:")
print(df_scalat[coloane_de_scalat].head())


# Exercitiul 8
X = df_scalat.drop(columns=['performance_level', 'math score', 'reading score', 'writing score', 'average_score'])
y = df_scalat['performance_level']

print(f"Dimensiunea X: {X.shape}")
print(f"Dimensiunea y: {y.shape}")


# Exercitiul 9
print("Cele mai importante caracteristici pentru predictie:")
print("- average_score (cel mai relevant - media tuturor notelor)")
print("- is_prepared (cursul de pregatire influenteaza performanta)")
print("- parental level of education (educatia parintilor)")

print("\nImpact scalare:")
print("Datele au acum media 0 si deviatia 1, comparabile intre ele.")
print("Esential pentru algoritmi bazati pe distanta (KNN, SVM).")

print("\nProbleme fara feature selection:")
print("- Model mai lent si predispus la overfitting")
print("- Caracteristici irelevante adauga zgomot")
print("- Interpretarea modelului devine mai dificila")