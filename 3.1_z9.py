imie = input("Podaj imię: ")
print("Witaj", imie)

wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

print("Twoje inicjały:", f"{imie[0]} {nazwisko[0]}")

lancuch = input("tekst: ")
for i in range(5):
    print(lancuch) 

text1 = input("tekst1: ")
text2 = input("tekst2: ")
polaczone = text1 + text2
print("Połączone:", polaczone)


s1 = input("tekst1: ")
s2 = input("tekst2: ")

polowa1 = len(s1) // 2
polowa2 = len(s2) // 2

nowy = s1[:polowa1] + s2[polowa2:]
print("Trzeci tekst:", nowy)
