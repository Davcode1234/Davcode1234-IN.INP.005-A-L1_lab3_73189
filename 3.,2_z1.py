Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]

print("Lista:", Moja_lista)

print("Długość listy:", len(Moja_lista))

print("Największy element:", max(Moja_lista))
print("Najmniejszy element:", min(Moja_lista))

print("Suma elementów:", sum(Moja_lista))

posortowana = sorted(Moja_lista)
print("Posortowana (sorted):", posortowana)

Moja_lista.append(100)
print("Po append(100):", Moja_lista)

Moja_lista.insert(2, 999)
print("Po insert(2, 999):", Moja_lista)

ostatni = Moja_lista.pop()
print("Po pop():", Moja_lista)

Moja_lista.reverse()
print("Po reverse():", Moja_lista)

lista1 = [1, 2, 3]
lista2 = [4, 5]
listaL = lista1 + lista2
print("Połączenie list lista1 + lista2:", listaL)

listaM = lista1 * 5
print("Pięciokrotne powtórzenie lista1:", listaM)

print("Pierwsze 3 elementy listaL[ :3]:", listaL[:3])
print("Od indeksu 2 do końca listaL[2: ]:", listaL[2:])
print("Co drugi element listaL[0:len(listaL):2]:", listaL[0:len(listaL):2])
print("Odwrócona listaL listaL[::-1]:", listaL[::-1])