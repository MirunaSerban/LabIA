#exercitiul 2
while True:
    nota_input = input("Introdu nota obținută la examen: ")
    nota = float(nota_input)

    if nota < 1 or nota > 10:
        print("Notă invalidă! Te rog să reintroduci o valoare validă între 1 și 10.")
    elif nota >= 9:
        print("Calificativ: Excelent")
        break
    elif nota >= 7:
        print("Calificativ: Bine")
        break
    elif nota >= 5:
        print("Calificativ: Suficient")
        break
    else:
        print("Calificativ: Reexaminare")
        break

#exercitiul 3
import random

numar_secret = random.randint(1, 50)
incercari = 0

print("Am ales un număr între 1 și 50. Încearcă să îl ghicești!")

while True:
    try:
        ghicit = int(input("Ghicește numărul (1-50): "))
        incercari += 1

        if ghicit < numar_secret:
            print("Numărul este mai mare!")
        elif ghicit > numar_secret:
            print("Numărul este mai mic!")
        else:
            print(f"Felicitări! Ai ghicit numărul în {incercari} încercări.")
            break
    except ValueError:
        print("Te rog introdu un număr valid.")


#exercitiul 4
orase = ["București", "Cluj-Napoca", "Timișoara", "Iași", "Sibiu"]

for index, oras in enumerate(orase, start=1):
    print(f"{index}. {oras}")


#exercitiul 5
import random

print("Bine ai venit la Loteria Python! Alege 6 numere între 1 și 49.")
numere_alese = []

for i in range(1, 7):
    numar = int(input(f"Numărul {i}: "))
    numere_alese.append(numar)

# Generăm 6 numere unice aleatorii între 1 și 49
numere_extrase = random.sample(range(1, 50), 6)
print(f"\nNumere extrase: {numere_extrase}")

# Găsim numerele comune
numere_ghicite = list(set(numere_alese).intersection(set(numere_extrase)))

print(f"Ai ghicit {len(numere_ghicite)} numere: {numere_ghicite}")

if len(numere_ghicite) >= 3:
    print("Felicitări! Ai câștigat un premiu mic!")
elif len(numere_ghicite) == 6:
    print("JACKPOT! Ai câștigat marele premiu!")
else:
    print("Nu ai câștigat. Mai încearcă!")


#exercitiul 6
inventar = []

print("Ai intrat într-o pădure magică.")
alegere1 = input("Mergi la stânga sau la dreapta? (stanga/dreapta): ").lower()

if alegere1 == "stanga":
    print("Te întâlnești cu un lup fioros!")
    actiune = input("Fugi sau lupți? (fugi/lupti): ").lower()
    if actiune == "fugi":
        print("Ai scăpat cu bine, dar te-ai întors la intrare.")
    else:
        print("Ai învins lupul și ai găsit o Sabie Magică!")
        inventar.append("Sabie Magică")

elif alegere1 == "dreapta":
    print("Ai găsit o comoară ascunsă sub un copac bătrân!")
    inventar.append("Monede de aur")
else:
    print("Nu ai ales nicio direcție și te-ai rătăcit.")

print(f"Inventarul tău final: {inventar}")


#exercitiul 7
comentariu = input("Introdu un comentariu: ").lower()

cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
cuvinte_negative = ["urât", "prost", "groaznic", "dezamăgitor"]

# Verificăm prezența cuvintelor
este_pozitiv = any(cuvant in comentariu for cuvant in cuvinte_pozitive)
este_negativ = any(cuvant in comentariu for cuvant in cuvinte_negative)

if este_pozitiv and not este_negativ:
    print("Comentariu pozitiv!")
elif este_negativ and not este_pozitiv:
    print("Comentariu negativ!")
else:
    print("Comentariu neutru.")


#exercitiul 8
import time

tari_risc = ["Coreea de Nord", "Siria", "Iran"]
tranzactii_suspecte = 0
numar_tranzactii = 0
timp_start = time.time()

print("Sistem de procesare tranzacții (scrie 'stop' la suma pentru a opri)")

while True:
    if tranzactii_suspecte >= 3:
        print("\n3 tranzacții suspecte detectate! Cont blocat.")
        break

    suma_input = input("\nIntrodu suma: ")
    if suma_input.lower() == 'stop':
        break

    suma = float(suma_input)
    tara = input("Introdu țara de proveniență: ")
    numar_tranzactii += 1

    # 1. Verificare BOT (peste 3 tranzacții în mai puțin de 60 de secunde)
    timp_curent = time.time()
    if numar_tranzactii > 3 and (timp_curent - timp_start) < 60:
        print(f"Tranzacție din {tara} → FRAUDĂ BOT (Prea multe acțiuni rapide)")
        tranzactii_suspecte += 1
        numar_tranzactii = 0  # resetăm contorul pentru următorul minut
        timp_start = time.time()
        continue

    # 2. Verificare Sumă și Țară
    if tara in tari_risc:
        print(f"Tranzacție: {suma} RON din {tara} → Frauduloasă (țară cu risc ridicat)")
        tranzactii_suspecte += 1
    elif suma > 10000:
        print(f"Tranzacție: {suma} RON din {tara} → Suspicioasă (sumă mare)")
        tranzactii_suspecte += 1
    else:
        print(f"Tranzacție: {suma} RON din {tara} → Sigură")