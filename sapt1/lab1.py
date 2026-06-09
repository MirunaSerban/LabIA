# Exercitiul 1
varsta = 22
nume = "Alex"
inaltime = 1.78
student = True

print(type(varsta))
print(type(nume))
print(type(inaltime))
print(type(student))


# Exercitiul 2
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# Exercitiul 3
mesaj = "Salut, eu sunt student la informatica"

print(len(mesaj))
print(mesaj.upper())
print(mesaj.lower())
print(mesaj.replace("student", "elev"))
print(mesaj.split(" "))
print(mesaj[0:5])


# Exercitiul 4
numere = [10, 25, 3, 47, 8, 19, 56]

print(numere)
print(len(numere))
print(min(numere))
print(max(numere))
print(sum(numere))
print(sorted(numere))

numere.append(100)
print(numere)

numere.remove(3)
print(numere)


# Exercitiul 5
student = {
    "nume": "Maria",
    "varsta": 21,
    "specializare": "Informatica",
    "an": 2
}

print(student["nume"])
print(student["varsta"])

student["medie"] = 9.50
print(student)

print(list(student.keys()))
print(list(student.values()))


# Exercitiul 6
fructe = ("mar", "para", "banana", "mar", "portocala", "mar")

print(fructe)
print(len(fructe))
print(fructe.count("mar"))
print(fructe.index("banana"))


# Exercitiul 7
lista_cu_duplicate = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
set_unic = set(lista_cu_duplicate)

print(lista_cu_duplicate)
print(set_unic)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))


# Exercitiul 8
nume = input("Cum te numesti? ")
varsta = int(input("Ce varsta ai? "))

print(f"Salut, {nume}! Ai {varsta} ani.")
print(f"La anul vei avea {varsta + 1} ani.")