import random
from functools import reduce
import datetime


# Exercitiul 1
def joc_piatra_foarfeca_hartie():
    while True:
        j1 = input("Jucator 1 (piatra/foarfeca/hartie): ").lower()
        j2 = input("Jucator 2 (piatra/foarfeca/hartie): ").lower()

        if j1 == j2:
            print("Egalitate!")
        elif (j1 == "piatra" and j2 == "foarfeca") or \
             (j1 == "foarfeca" and j2 == "hartie") or \
             (j1 == "hartie" and j2 == "piatra"):
            print("Felicitari Jucator 1! Ai castigat!")
        else:
            print("Felicitari Jucator 2! Ai castigat!")

        raspuns = input("Mai jucati o tura? (da/nu): ").lower()
        if raspuns != "da":
            print("La revedere!")
            break

joc_piatra_foarfeca_hartie()


# Exercitiul 2
def genereaza_factura(client, **produse):
    print(f"Factura pentru: {client}")
    print("-" * 30)
    total = 0
    for produs, pret in produse.items():
        print(f"{produs}: {pret} lei")
        total += pret
    print("-" * 30)
    print(f"Total: {total} lei")

genereaza_factura("Maria", paine=5, lapte=8, branza=15, oua=12)


# Exercitiul 3
def normalize_data(lista):
    minim = min(lista)
    maxim = max(lista)
    return [(x - minim) / (maxim - minim) for x in lista]

data = [10, 20, 30, 40, 50]
normalized_data = normalize_data(data)
print(normalized_data)


# Exercitiul 4
patrat = lambda lista: [x ** 2 for x in lista]

my_list = [1, 2, 3, 4, 5]
print(patrat(my_list))


# Exercitiul 5
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
sorted_a = sorted(a, key=lambda x: x[1])
print(sorted_a)


# Exercitiul 6
orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x % 2 == 0, orig_list))
odd_list = list(filter(lambda x: x % 2 != 0, orig_list))

print(f"Pare: {even_list}")
print(f"Impare: {odd_list}")


# Exercitiul 7
preturi = [100, None, 200, 50, None, 300, 75]

preturi_filtrate = list(filter(lambda x: x is not None, preturi))
preturi_reduse = list(map(lambda x: x * 0.9, preturi_filtrate))

print(f"Preturi initiale: {preturi}")
print(f"Dupa filtrare: {preturi_filtrate}")
print(f"Dupa reducere 10%: {preturi_reduse}")


# Exercitiul 8
data_curenta = datetime.datetime.now()

an = lambda d: d.year
luna = lambda d: d.month
zi = lambda d: d.day
ora = lambda d: d.time()

print(data_curenta)
print(an(data_curenta))
print(luna(data_curenta))
print(zi(data_curenta))
print(ora(data_curenta))


# Exercitiul 9
def sum_lists(l1, l2):
    return list(map(lambda pereche: pereche[0] + pereche[1], zip(l1, l2)))

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
result = sum_lists(list1, list2)
print(result)


# Exercitiul 10
pare = [x for x in range(0, 101) if x % 2 == 0]
print(pare)

cuburi = [x ** 3 for x in range(1, 11)]
print(cuburi)

lista_a = [1, 2, 3, 4, 5, 6]
lista_b = [4, 5, 6, 7, 8, 9]
comune = [x for x in lista_a if x in lista_b]
print(comune)


# Exercitiul 11
primele_10_pare = {x for x in range(2, 21) if x % 2 == 0}
print(primele_10_pare)

text = "informatica"
litere_distincte = {c for c in text}
print(litere_distincte)

propozitie = "Acesta este un exemplu pentru programare in python"
cuvinte_lungi = {cuvant for cuvant in propozitie.split() if len(cuvant) >= 5}
print(cuvinte_lungi)


# Exercitiul 12
patrate = {x: x ** 2 for x in range(1, 11)}
print(patrate)

text = "programare"
aparitii = {litera: text.count(litera) for litera in text}
print(aparitii)

divizori = {x: [d for d in range(1, x + 1) if x % d == 0] for x in range(1, 11)}
print(divizori)