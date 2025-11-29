# Zadanie 2
imiona = ["Michał", "Bartek", "Natalia", "Dawid"]
print("Początkowa lista:", imiona)

imiona.sort()
print("Posortowana lista:", imiona)

imiona.append("Ola")
imiona.append("Paweł")
print("Po dodaniu dwóch osób:", imiona)

ostatnia_osoba = imiona.pop() 
print("Po pop():", imiona)
print("Usunięta (ostatnia) osoba:", ostatnia_osoba)

imiona.insert(2, "Tomek")
print("Po insert(2, 'Tomek'):", imiona)

imiona.reverse()
print("Po reverse():", imiona)

imiona_zdublowane = imiona * 2
print("Zdublowana lista:", imiona_zdublowane)