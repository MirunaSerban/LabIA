import random


# Exercitiul 1
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for linie in picture:
    for pixel in linie:
        if pixel == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Exercitiul 2
while True:
    nota = int(input("Introdu nota: "))
    if nota < 1 or nota > 10:
        print("Nota invalida! Reintroduceti.")
        continue
    if nota >= 9:
        print("Excelent")
    elif nota >= 7:
        print("Bine")
    elif nota >= 5:
        print("Suficient")
    else:
        print("Reexaminare")
    break


# Exercitiul 3
numar_secret = random.randint(1, 50)
incercari = 0

while True:
    ghicit = int(input("Ghiceste numarul (1-50): "))
    incercari += 1
    if ghicit < numar_secret:
        print("Numarul este mai mare!")
    elif ghicit > numar_secret:
        print("Numarul este mai mic!")
    else:
        print(f"Felicitari! Ai ghicit numarul in {incercari} incercari.")
        break


# Exercitiul 4
orase = ["Bucuresti", "Cluj-Napoca", "Timisoara", "Iasi", "Constanta", "Sibiu"]

for index, oras in enumerate(orase, start=1):
    print(f"{index}. {oras}")


# Exercitiul 5
print("Bine ai venit la Loteria Python!")
print("Alege 6 numere intre 1 si 49.")

numere_alese = []
for i in range(6):
    while True:
        n = int(input(f"Numarul {i+1}: "))
        if n < 1 or n > 49:
            print("Numar invalid! Reincearca.")
        elif n in numere_alese:
            print("Numarul a fost deja ales! Reincearca.")
        else:
            numere_alese.append(n)
            break

numere_extrase = random.sample(range(1, 50), 6)
print(f"Numere extrase: {numere_extrase}")

ghicite = [n for n in numere_alese if n in numere_extrase]
print(f"Ai ghicit {len(ghicite)} numere: {ghicite}")

if len(ghicite) == 6:
    print("JACKPOT! Ai castigat premiul cel mare!")
elif len(ghicite) >= 4:
    print("Felicitari! Ai castigat un premiu mare!")
elif len(ghicite) >= 2:
    print("Felicitari! Ai castigat un premiu mic!")
else:
    print("Mai incearca data viitoare!")


# Exercitiul 6
inventar = []
print("Bine ai venit in padurea magica!")

directie = input("Alegi stanga sau dreapta? ")

if directie == "stanga":
    print("Ai intalnit un lup! Ai reusit sa fugi.")
    directie2 = input("Continui? stanga sau dreapta? ")
    if directie2 == "stanga":
        print("Ai gasit o sabie magica!")
        inventar.append("sabie magica")
    else:
        print("Ai gasit o harta veche!")
        inventar.append("harta")
elif directie == "dreapta":
    print("Ai descoperit o comoara!")
    inventar.append("monede de aur")
    directie2 = input("Continui? stanga sau dreapta? ")
    if directie2 == "stanga":
        print("Ai gasit un elixir!")
        inventar.append("elixir")
    else:
        print("Ai gasit un cristal!")
        inventar.append("cristal")
else:
    print("Te-ai ratacit in padure...")

print(f"Inventarul tau: {inventar}")


# Exercitiul 7
cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
cuvinte_negative = ["urat", "prost", "groaznic", "dezamagitor"]

comentariu = input("Introdu un comentariu: ").lower()

pozitiv = False
negativ = False

for cuvant in cuvinte_pozitive:
    if cuvant in comentariu:
        pozitiv = True
        break

for cuvant in cuvinte_negative:
    if cuvant in comentariu:
        negativ = True
        break

if pozitiv and not negativ:
    print("Comentariu pozitiv!")
elif negativ and not pozitiv:
    print("Comentariu negativ!")
else:
    print("Comentariu neutru.")


# Exercitiul 8
tari_risc = ["Coreea de Nord", "Siria", "Iran"]
tranzactii_suspecte = 0

print("Procesam tranzactiile...")

while True:
    suma = float(input("Suma tranzactiei (sau 0 pentru a opri): "))
    if suma == 0:
        break
    tara = input("Tara: ")

    if tara in tari_risc:
        print(f"Tranzactie: {suma} RON din {tara} -> Frauduloasa (tara cu risc ridicat)")
        tranzactii_suspecte += 1
    elif suma > 10000:
        print(f"Tranzactie: {suma} RON din {tara} -> Suspicioasa (suma mare)")
        tranzactii_suspecte += 1
    else:
        print(f"Tranzactie: {suma} RON din {tara} -> Sigura")

    if tranzactii_suspecte >= 3:
        print(f"{tranzactii_suspecte} tranzactii suspecte detectate! Cont blocat.")
        break