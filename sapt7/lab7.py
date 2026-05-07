import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


# Exercitiul 1
iris = load_iris()
print(f"Numar de exemple: {iris.data.shape[0]}")
print(f"Numar de caracteristici: {iris.data.shape[1]}")
print(f"Caracteristici: {iris.feature_names}")
print(f"Clase: {iris.target_names}")


# Exercitiul 2
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"X_train: {X_train.shape}")
print(f"X_test:  {X_test.shape}")
print(f"y_train: {y_train.shape}")
print(f"y_test:  {y_test.shape}")


# Exercitiul 3
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Inainte de scalare:")
print(X_train[:3])
print("Dupa scalare:")
print(X_train_scaled[:3])


# Exercitiul 4
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
acuratete = accuracy_score(y_test, y_pred)
print(f"Acuratetea cu k=3: {acuratete:.4f}")


# Exercitiul 5
acuratete_k = []
valori_k = range(1, 16)

for k in valori_k:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(X_train_scaled, y_train)
    y_pred_temp = knn_temp.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred_temp)
    acuratete_k.append(acc)
    print(f"k={k} -> Acuratete: {acc:.4f}")

plt.figure(figsize=(10, 5))
plt.plot(valori_k, acuratete_k, 'o-', markersize=8, color='steelblue')
plt.xlabel('Valoarea lui k')
plt.ylabel('Acuratetea')
plt.title('Acuratetea KNN in functie de k')
plt.grid(True, alpha=0.3)
plt.xticks(valori_k)
plt.show()

k_optim = valori_k[np.argmax(acuratete_k)]
print(f"K optim: {k_optim}")


# Exercitiul 6
cm = confusion_matrix(y_test, y_pred)
print("Matricea de confuzie:")
print(cm)

plt.figure(figsize=(7, 5))
plt.imshow(cm, cmap='Blues')
plt.colorbar()
plt.xticks(range(3), iris.target_names)
plt.yticks(range(3), iris.target_names)
plt.xlabel('Clasa prezisa')
plt.ylabel('Clasa reala')
plt.title('Matricea de confuzie')
for i in range(3):
    for j in range(3):
        plt.text(j, i, str(cm[i, j]), ha='center', va='center',
                 color='red', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

print("Raport de clasificare:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))


# Exercitiul 7
plt.figure(figsize=(10, 6))
culori = ['red', 'green', 'blue']
for i in range(3):
    mask = iris.target == i
    plt.scatter(iris.data[mask, 2], iris.data[mask, 3],
                color=culori[i], label=iris.target_names[i],
                alpha=0.7, edgecolors='black')

plt.xlabel('Lungime petala (cm)')
plt.ylabel('Latime petala (cm)')
plt.title('Iris: cele 3 specii in functie de petala')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

sepal_length = float(input("Lungime sepala (cm): "))
sepal_width = float(input("Latime sepala (cm): "))
petal_length = float(input("Lungime petala (cm): "))
petal_width = float(input("Latime petala (cm): "))

floare_noua = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
floare_noua_scaled = scaler.transform(floare_noua)
predictie = knn.predict(floare_noua_scaled)
print(f"Specia prezisa: {iris.target_names[predictie[0]]}")

probabilitati = knn.predict_proba(floare_noua_scaled)
print("Probabilitati:")
for i, prob in enumerate(probabilitati[0]):
    print(f"  {iris.target_names[i]}: {prob*100:.1f}%")