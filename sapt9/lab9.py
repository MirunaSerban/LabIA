import numpy as np
# pandas = lucreaza cu tabele (DataFrame-uri), ca un Excel in Python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score

# EXERCITIUL 1: Incarcam setul de date wine
print("=" * 60)
print("EXERCITIUL 1: Incarcare set de date Wine")
print("=" * 60)
wine = load_wine()
print("Setul de date contine:", wine.keys())
print(f"Numar de exemple: {wine.data.shape[0]}")
print(f"Numar de caracteristici: {wine.data.shape[1]}")
print(f"Numar de clase: {len(wine.target_names)}")

# EXERCITIUL 2: Afisam primele 5 randuri intr-un DataFrame
print("\n" + "=" * 60)
print("EXERCITIUL 2: Primele 5 randuri")
print("=" * 60)
# Metoda 1: Cream noi DataFrame-ul
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
df['target'] = wine.target
# Metoda 2 (cea ceruta in cerinta - cu as_frame):
print(df.head())

# EXERCITIUL 3: Listam toate caracteristicile
print("\n" + "=" * 60)
print("EXERCITIUL 3: Numele caracteristicilor")
print("=" * 60)
print("Caracteristici (13):")
for i, nume in enumerate(wine.feature_names, start=1):
    print(f"  {i}. {nume}")

print("\nClase (3 tipuri de vin):")
print(wine.target_names)

# EXERCITIUL 4: Antrenarea unui arbore de decizie pe 2 caracteristici
print("\n" + "=" * 60)
print("EXERCITIUL 4: Arbore de decizie cu max_depth=2")
print("=" * 60)

#Selectam DOAR 2 caracteristici: alcohol si flavanoids
X = df[['alcohol', 'flavanoids']]
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Cream arborele cu adancime maxima 2
model = DecisionTreeClassifier(max_depth=2, random_state=42)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acuratete = accuracy_score(y_test, y_pred)
print(f"Acuratetea modelului (max_depth=2): {acuratete:.4f}")
print(f"Adica {acuratete*100:.2f}% din predictii sunt corecte")
print("\nSe deschide fereastra cu arborele...")
plt.figure(figsize=(12, 6))
plot_tree(model,
          feature_names=['alcohol', 'flavanoids'],
          class_names=wine.target_names,
          filled=True,
          rounded=True)
plt.title("Arbore de decizie (max_depth=2)")
plt.show()


# EXERCITIUL 5: Arbore complet (fara limita de adancime)
print("\n" + "=" * 60)
print("EXERCITIUL 5: Arbore complet (max_depth=None)")
print("=" * 60)
model_complet = DecisionTreeClassifier(max_depth=None, random_state=42)
model_complet.fit(X_train, y_train)
y_pred_complet = model_complet.predict(X_test)

acuratete_complet = accuracy_score(y_test, y_pred_complet)
print(f"Acuratetea arborelui complet: {acuratete_complet:.4f}")
print(f"Adica {acuratete_complet*100:.2f}% din predictii sunt corecte")

print(f"\nComparatie:")
print(f"  Arbore cu max_depth=2:   {acuratete:.4f}")
print(f"  Arbore complet:           {acuratete_complet:.4f}")
print("Atentie: arborele complet poate face OVERFITTING!")

# EXERCITIUL 6: Arbore pe TOATE cele 13 caracteristici
print("\n" + "=" * 60)
print("EXERCITIUL 6: Arbore pe toate cele 13 caracteristici")
print("=" * 60)

X_full = df[wine.feature_names]
y_full = df['target']

X_full_train, X_full_test, y_full_train, y_full_test = train_test_split(
    X_full, y_full, test_size=0.2, random_state=42
)
model_full = DecisionTreeClassifier(random_state=42)
model_full.fit(X_full_train, y_full_train)

y_full_pred = model_full.predict(X_full_test)
acuratete_full = accuracy_score(y_full_test, y_full_pred)
print(f"Acuratetea cu toate caracteristicile: {acuratete_full:.4f}")
print("\nImportanta fiecarei caracteristici:")
importante = model_full.feature_importances_

caracteristici_importante = list(zip(wine.feature_names, importante))
caracteristici_importante.sort(key=lambda x: x[1], reverse=True)

for nume, imp in caracteristici_importante:
    if imp > 0:
        print(f"  {nume:30s}: {imp:.4f} ({imp*100:.2f}%)")

print("\nSe deschide graficul cu importanta caracteristicilor...")
plt.figure(figsize=(10, 6))

nume_sortate = [x[0] for x in caracteristici_importante]
valori_sortate = [x[1] for x in caracteristici_importante]

plt.barh(nume_sortate, valori_sortate, color='steelblue')
plt.xlabel('Importanta')
plt.title('Importanta caracteristicilor in arborele de decizie')
plt.gca().invert_yaxis()  # cel mai important sus
plt.tight_layout()
plt.show()

# EXERCITIUL 7 (BONUS): Mini-arbore pe hartie - calcul Gini
print("\n" + "=" * 60)
print("EXERCITIUL 7 (BONUS): Calcul Gini pe un subset")
print("=" * 60)

subset = df[['alcohol', 'flavanoids', 'target']].head(6)
print("Subset cu 6 exemple:")
print(subset)

# Numaram cate exemple sunt din fiecare clasa
from collections import Counter
counter = Counter(subset['target'])
total = len(subset)
print(f"\nDistributia claselor in subset: {dict(counter)}")
gini = 1
for clasa, count in counter.items():
    p = count / total
    gini -= p ** 2

print(f"Gini pentru nodul radacina: {gini:.4f}")
print("(0 = pur, valoare mai mare = mai amestecat)")