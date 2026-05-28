import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0



# EXTRA 1: Afiseaza primele 9 imagini din set intr-o grila

print("=" * 60)
print("EXTRA 1: Afisare primele 9 cifre")
print("=" * 60)

plt.figure(figsize=(8, 8))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Eticheta: {y_train[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()


# EXTRA 2: Cate exemple avem din fiecare cifra?

print("\n" + "=" * 60)
print("EXTRA 2: Cate exemple din fiecare cifra")
print("=" * 60)

cifre, aparitii = np.unique(y_train, return_counts=True)
for cifra, count in zip(cifre, aparitii):
    print(f"Cifra {cifra}: {count} exemple")

plt.figure(figsize=(8, 5))
plt.bar(cifre, aparitii, color='steelblue')
plt.xlabel('Cifra')
plt.ylabel('Numar de exemple')
plt.title('Cate exemple avem din fiecare cifra')
plt.xticks(cifre)
plt.show()



# EXTRA 3: Antreneaza un model si urmareste cum scade eroarea

print("\n" + "=" * 60)
print("EXTRA 3: Urmarim cum invata modelul")
print("=" * 60)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Salvam istoricul antrenarii ca sa-l putem afisa pe grafic
istoric = model.fit(x_train, y_train, epochs=5)

# Graficul acuratetei pe fiecare epoca
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(istoric.history['accuracy'], 'o-', color='green')
plt.xlabel('Epoca')
plt.ylabel('Acuratete')
plt.title('Acuratetea creste cu fiecare epoca')

plt.subplot(1, 2, 2)
plt.plot(istoric.history['loss'], 'o-', color='red')
plt.xlabel('Epoca')
plt.ylabel('Eroare (loss)')
plt.title('Eroarea scade cu fiecare epoca')

plt.tight_layout()
plt.show()


# EXTRA 4: Gaseste o imagine pe care modelul o prezice GRESIT

print("\n" + "=" * 60)
print("EXTRA 4: Cauta o predictie gresita")
print("=" * 60)

# Facem predictii pe primele 100 de imagini din test
predictii = model.predict(x_test[:100])
cifre_prezise = np.argmax(predictii, axis=1)

for i in range(100):
    if cifre_prezise[i] != y_test[i]:
        print(f"Gasit! La indexul {i}:")
        print(f"  Eticheta reala: {y_test[i]}")
        print(f"  Cifra prezisa:  {cifre_prezise[i]}")

        plt.figure(figsize=(5, 5))
        plt.imshow(x_test[i], cmap='gray')
        plt.title(f"Real: {y_test[i]} | Model a zis: {cifre_prezise[i]} (GRESIT)")
        plt.axis('off')
        plt.show()
        break
else:
    print("Modelul a prezis corect toate primele 100 imagini!")



# EXTRA 5: Afiseaza cat de "sigur" e modelul pe o predictie
print("\n" + "=" * 60)
print("EXTRA 5: Cat de increzator e modelul")
print("=" * 60)

index = 0
imagine = x_test[index]
predictie = model.predict(np.expand_dims(imagine, axis=0))[0]

print(f"Eticheta reala: {y_test[index]}")
print("\nProbabilitatile pentru fiecare cifra:")
for cifra in range(10):
    procent = predictie[cifra] * 100
    bara = '#' * int(procent / 2)  # bara vizuala simpla
    print(f"  Cifra {cifra}: {procent:5.1f}% {bara}")

cifra_prezisa = np.argmax(predictie)
print(f"\nModelul prezice: {cifra_prezisa} cu {predictie[cifra_prezisa]*100:.1f}% incredere")

# EXTRA 6: Compara doua modele - unul mic vs unul mare

print("\n" + "=" * 60)
print("EXTRA 6: Model mic vs model mare")
print("=" * 60)

# Model mic - putini neuroni
model_mic = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
model_mic.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print("Antrenam modelul mic (16 neuroni)...")
model_mic.fit(x_train, y_train, epochs=3, verbose=0)
_, acc_mic = model_mic.evaluate(x_test, y_test, verbose=0)

# Model mare - mai multe straturi
model_mare = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
model_mare.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print("Antrenam modelul mare (256 + 128 neuroni)...")
model_mare.fit(x_train, y_train, epochs=3, verbose=0)
_, acc_mare = model_mare.evaluate(x_test, y_test, verbose=0)

print(f"\nAcuratete model mic (16 neuroni):        {acc_mic:.4f}")
print(f"Acuratete model mare (256+128 neuroni):  {acc_mare:.4f}")
print("Observatie: modelul mai mare e de obicei mai bun,")
print("dar diferenta nu e mereu mare pentru un set simplu ca MNIST.")



# EXTRA 7: Deseneaza tu o cifra modificand pixelii

print("\n" + "=" * 60)
print("EXTRA 7: Cream o imagine goala si o testam")
print("=" * 60)

# Cream o imagine complet neagra (toate valorile 0)
imagine_goala = np.zeros((28, 28))

# "Desenam" o linie verticala simpla (ca un 1)
imagine_goala[5:23, 14] = 1.0  # coloana 14, randurile 5-22

predictie = model.predict(np.expand_dims(imagine_goala, axis=0))[0]
cifra_prezisa = np.argmax(predictie)

plt.figure(figsize=(5, 5))
plt.imshow(imagine_goala, cmap='gray')
plt.title(f"Cifra desenata de noi | Model: {cifra_prezisa}")
plt.axis('off')
plt.show()

print(f"Am desenat o linie verticala simpla.")
print(f"Modelul a prezis: {cifra_prezisa}")
print("(probabil prezice 1, pentru ca seamana cu un 1)")