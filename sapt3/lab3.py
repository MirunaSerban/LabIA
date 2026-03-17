#exercitiul 2
nota = float(input ("Introdu nota: "))
if nota <1 or nota >10:
    print("Reintroduceti nota! ")

if nota <5 :
   print ("Reexaminare")
elif nota <=6:
    print ("Suficient")
elif nota <=8:
    print ("Bine")
elif nota <=10:
    print ("Excelent")

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