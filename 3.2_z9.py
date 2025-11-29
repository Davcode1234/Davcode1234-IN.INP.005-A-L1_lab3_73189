zakupy = {
    "chleb": 5.00,
    "kurczak": 14.50,
    "masło": 8.20,
    "ser": 10.00
}
for artykul, kwota in zakupy.items():
    print(artykul, ":", kwota, "zł")

suma = 0
for kwota in zakupy.values():
    suma += kwota

print("Suma wydatków:", suma, "zł")