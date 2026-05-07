import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# EXERCITIUL 1: Incarcam setul de date diabetes
print("=" * 60)
print("EXERCITIUL 1: Incarcare set de date")
print("=" * 60)
diabetes = load_diabetes()
print("Setul de date contine:", diabetes.keys())

# EXERCITIUL 2: Afisam primele 5 randuri intr-un DataFrame Pandas
print("\n" + "=" * 60)
print("EXERCITIUL 2: Primele 5 randuri")
print("=" * 60)
df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target
print(df.head(5))

# EXERCITIUL 3: Listam toate caracteristicile (numele coloanelor)

print("\n" + "=" * 60)
print("EXERCITIUL 3: Numele caracteristicilor")
print("=" * 60)
print("Caracteristici:", diabetes.feature_names)

# EXERCITIUL 4: Informatii statistice (medie, deviatie standard, min, max)
print("\n" + "=" * 60)
print("EXERCITIUL 4: Statistici descriptive")
print("=" * 60)
print(df.describe())

# EXERCITIUL 5: Histograma pentru BMI

print("\n" + "=" * 60)
print("EXERCITIUL 5: Histograma BMI")
print("=" * 60)
print("Se deschide o fereastra cu graficul...")

plt.hist(df['bmi'], bins=20, edgecolor='black')
plt.title('Distributia valorilor BMI')
plt.xlabel('BMI (valoare normalizata)')
plt.ylabel('Numar de pacienti')
plt.show()

# EXERCITIUL 6: Grafice scatter pentru BMI si varsta vs target

print("\n" + "=" * 60)
print("EXERCITIUL 6: Grafice BMI si Varsta vs Target")
print("=" * 60)
print("Se deschide o fereastra cu 2 grafice alaturate...")

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(df['bmi'], df['target'], alpha=0.5)
plt.xlabel('BMI')
plt.ylabel('Progresia bolii (target)')
plt.title('BMI vs Progresia bolii')

# subplot(1, 2, 2) = aceeasi grila, dar pozitia 2 (dreapta)
plt.subplot(1, 2, 2)
plt.scatter(df['age'], df['target'], alpha=0.5, color='orange')
plt.xlabel('Varsta')
plt.ylabel('Progresia bolii (target)')
plt.title('Varsta vs Progresia bolii')

# tight_layout aranjeaza graficele frumos sa nu se suprapuna
plt.tight_layout()
plt.show()

# EXERCITIUL 7: Regresie liniara simpla folosind doar BMI

print("\n" + "=" * 60)
print("EXERCITIUL 7: Regresie liniara simpla cu BMI")
print("=" * 60)
X = df[['bmi']]
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Date antrenare: {X_train.shape[0]} exemple")
print(f"Date testare:   {X_test.shape[0]} exemple")
#  Antrenarea modelului de regresie liniara
model = LinearRegression()
model.fit(X_train, y_train)
print(f"Panta (m / coeficient): {model.coef_[0]:.2f}")
print(f"Interceptul (b):         {model.intercept_:.2f}")
y_pred = model.predict(X_test)

# Reprezentam grafic datele de testare si linia de regresie
print("Se deschide graficul cu linia de regresie...")

plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color='blue', alpha=0.5, label='Date reale')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Linia de regresie')
plt.xlabel('BMI')
plt.ylabel('Progresia bolii')
plt.title('Regresie liniara: BMI -> Progresia bolii')
plt.legend()  # afiseaza legenda (cu numele liniilor)
plt.show()

#  Calculam MSE
mse = mean_squared_error(y_test, y_pred)
print(f"MSE (Mean Squared Error): {mse:.2f}")
r2 = model.score(X_test, y_test)
print(f"R² (cat de bun e modelul): {r2:.4f}")

# EXERCITIUL 8: Regresie pe DOUA caracteristici (BMI si BP)
print("\n" + "=" * 60)
print("EXERCITIUL 8: Regresie liniara cu BMI si BP")
print("=" * 60)

# 8.a: Selectam BMI si BP ca input
X2 = df[['bmi', 'bp']]
y2 = df['target']  # target-ul ramane acelasi
X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y2, test_size=0.2, random_state=42
)

# Se antreneaza un nou model
model2 = LinearRegression()
model2.fit(X2_train, y2_train)
print("Coeficientii modelului:")
for nume, coef in zip(['bmi', 'bp'], model2.coef_):
    print(f"  {nume}: {coef:.2f}")
print(f"Interceptul: {model2.intercept_:.2f}")

# 8.d: Calculam scorul R² pe setul de testare

# .score() pe un model de regresie returneaza R²
r2_model2 = model2.score(X2_test, y2_test)
print(f"R² al modelului cu 2 caracteristici: {r2_model2:.4f}")

# Comparam cu modelul de la exercitiul 7
print(f"R² al modelului cu 1 caracteristica (BMI): {r2:.4f}")
print("=> Adaugand BP, modelul e (de obicei) un pic mai bun!")