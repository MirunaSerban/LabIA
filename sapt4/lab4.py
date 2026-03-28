#exercitiul 1
def ex1_rock_paper_scissors():
    print("--- Rock, Paper, Scissors ---")
    while True:
        j1 = input("Jucător 1 (piatra/hartia/foarfeca): ").lower()
        j2 = input("Jucător 2 (piatra/hartia/foarfeca): ").lower()

        if j1 == j2:
            print("Egalitate!")
        elif (j1 == "piatra" and j2 == "foarfeca") or \
                (j1 == "foarfeca" and j2 == "hartia") or \
                (j1 == "hartia" and j2 == "piatra"):
            print("Felicitări Jucător 1! Ai câștigat!")
        else:
            print("Felicitări Jucător 2! Ai câștigat!")

        mai_joci = input("Mai jucați o rundă? (da/nu): ").lower()
        if mai_joci != "da":
            break
#ex1_rock_paper_scissors()


# Exercitiul 2
def genereaza_factura(nume_client, **produse):
    print(f"--- Factură pentru {nume_client} ---")
    total = 0
    for produs, pret in produse.items():
        print(f"- {produs}: {pret} RON")
        total += pret
    print(f"Total de plată: {total} RON\n")

genereaza_factura("Miruna", Laptop=4500, Mouse=150, Tastatura=250)

#Exercitiul 3
def normalize_data(data):
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

data = [10, 20, 30, 40, 50]
print("Ex 3 Normalizare:", normalize_data(data))

#Exercitiul 4
my_list = [1, 2, 3]
patrate = list(map(lambda x: x**2, my_list))
print("Ex 4 Lista la pătrat:", patrate)

#Exercitiul 5
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
sorted_a = sorted(a, key=lambda x: x[1])
print("Ex 5 Sortare tupluri:", sorted_a)

#Exercitiul 6
orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x % 2 == 0, orig_list))
odd_list = list(filter(lambda x: x % 2 != 0, orig_list))

print("Ex 6 Pare:", even_list)
print("Ex 6 Impare:", odd_list)


#Exercitiul 7
preturi = [100, None, 200, 50, None, 300]
preturi_curatate = list(filter(lambda x: x is not None, preturi))
preturi_reduse = list(map(lambda x: x * 0.9, preturi_curatate))

print("Ex 7 Prețuri reduse:", preturi_reduse)


#Exercitiul 8
import datetime
acum = datetime.datetime.now()

extrage_an = lambda x: x.year
extrage_luna = lambda x: x.month
extrage_data_ora = lambda x: (x.date(), x.time())

print(f"Ex 8 An: {extrage_an(acum)}, Lună: {extrage_luna(acum)}, Dată și Oră: {extrage_data_ora(acum)}")


#Exercitiul 9
def sum_lists(l1, l2):
    return [x + y for x, y in zip(l1, l2)]

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
print("Ex 9 Suma liste:", sum_lists(list1, list2))

#Exercitiul 10
# Numere pare de la 0 la 100
pare_100 = [x for x in range(101) if x % 2 == 0]

# Cuburile primelor 10 numere întregi
cuburi = [x**3 for x in range(1, 11)]

# Elemente comune din două liste
lista_a = [1, 2, 3, 4, 5]
lista_b = [3, 4, 5, 6, 7]
comune = [x for x in lista_a if x in lista_b]

print("Ex 10 Cuburi:", cuburi)
print("Ex 10 Elemente comune:", comune)


#Exercitiul 11
text_test = "programare python la laborator"

# Primele 10 numere pare (0, 2, 4 ... 18)
set_pare = {x for x in range(20) if x % 2 == 0}

# Litere distincte dintr-un string (ignorând spațiile)
litere_distincte = {char for char in text_test if char != ' '}

# Cuvinte care au cel puțin 5 litere [cite: 114]
cuvinte_lungi = {word for word in text_test.split() if len(word) >= 5}

print("Ex 11 Cuvinte >= 5 litere:", cuvinte_lungi)

#Exercitiul 12
cuvant = "abracadabra"

# Pătratele numerelor 1-10
dict_patrate = {x: x**2 for x in range(1, 11)}

# Numărul de apariții ale fiecărei litere dintr-un string
aparitii_litere = {char: cuvant.count(char) for char in cuvant}

# Primele 10 numere ca chei și divizorii lor ca valori [cite: 117]
dict_divizori = {x: [d for d in range(1, x + 1) if x % d == 0] for x in range(1, 11)}

print("Ex 12 Apariții litere:", aparitii_litere)
print("Ex 12 Divizori:", dict_divizori)
