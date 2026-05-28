import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


# Exercitiul 1
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print(f"Imagini antrenare: {x_train.shape}")
print(f"Imagini testare: {x_test.shape}")

x_train = x_train / 255.0
x_test = x_test / 255.0

print(f"Valoare minima: {x_train.min()}")
print(f"Valoare maxima: {x_train.max()}")


# Exercitiul 2
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.summary()


# Exercitiul 3
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Acuratete pe test: {test_acc:.4f}")


# Exercitiul 4
index = 0
imagine = x_test[index]
predictie = model.predict(np.expand_dims(imagine, axis=0))
cifra_prezisa = np.argmax(predictie)

print(f"Eticheta reala: {y_test[index]}")
print(f"Cifra prezisa: {cifra_prezisa}")

plt.figure(figsize=(5, 5))
plt.imshow(imagine, cmap='gray')
plt.title(f"Real: {y_test[index]} | Prezis: {cifra_prezisa}")
plt.axis('off')
plt.show()


# Exercitiul 5
model_256 = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model_256.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

model_256.fit(x_train, y_train, epochs=5)

_, acc_256 = model_256.evaluate(x_test, y_test)
print(f"Acuratete cu 256 neuroni: {acc_256:.4f}")
print(f"Acuratete cu 128 neuroni: {test_acc:.4f}")


# Exercitiul 6
model_10ep = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model_10ep.compile(optimizer='adam',
                   loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])

model_10ep.fit(x_train, y_train, epochs=10)

_, acc_10ep = model_10ep.evaluate(x_test, y_test)
print(f"Acuratete cu 10 epoci: {acc_10ep:.4f}")


# Exercitiul 7
model_tanh = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='tanh'),
    keras.layers.Dense(10, activation='softmax')
])

model_tanh.compile(optimizer='adam',
                   loss='sparse_categorical_crossentropy',
                   metrics=['accuracy'])

model_tanh.fit(x_train, y_train, epochs=5)

_, acc_tanh = model_tanh.evaluate(x_test, y_test)
print(f"Acuratete cu tanh: {acc_tanh:.4f}")
print(f"Acuratete cu relu: {test_acc:.4f}")


# Exercitiul 8
(xf_train, yf_train), (xf_test, yf_test) = keras.datasets.fashion_mnist.load_data()

nume_clase = ['Tricou', 'Pantalon', 'Pulover', 'Rochie', 'Palton',
              'Sandala', 'Camasa', 'Adidas', 'Geanta', 'Gheata']

xf_train = xf_train / 255.0
xf_test = xf_test / 255.0

model_fashion = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model_fashion.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

model_fashion.fit(xf_train, yf_train, epochs=5)

_, acc_fashion = model_fashion.evaluate(xf_test, yf_test)
print(f"Acuratete pe Fashion-MNIST: {acc_fashion:.4f}")

index = 0
predictie_f = model_fashion.predict(np.expand_dims(xf_test[index], axis=0))
clasa_prezisa = np.argmax(predictie_f)

plt.figure(figsize=(5, 5))
plt.imshow(xf_test[index], cmap='gray')
plt.title(f"Real: {nume_clase[yf_test[index]]} | Prezis: {nume_clase[clasa_prezisa]}")
plt.axis('off')
plt.show()