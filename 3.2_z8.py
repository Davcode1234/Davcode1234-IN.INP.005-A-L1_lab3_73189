stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżancie",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)

ilosc_stopni = len(stopnie)
Major_index = stopnie.index("Major")
is_Pulkownik = "Pułkownik" in stopnie

print("Liczba stopni:", ilosc_stopni)
print("Indeks Major:", Major_index)
print("Czy jest pulkownik:", is_Pulkownik )