def volum():
    lengde=float(input("hva er lengden av objektet?"))
    bredde=float(input("hva er bredde av objektet?"))
    høyde=float(input("hva er høyde av objektet?"))

    volumen=lengde*bredde*høyde
    print(f"volumet er {volumen}")
    return
volum()

print("\nkoden under er laget av GPT UiO\n")

def calculate_volume(length, width, height):
    # Beregn volumet ved å multiplisere lengde, bredde og høyde
    volume = length * width * height
    # Returner volumet
    return volume

# Kall funksjonen med forskjellige verdier og skriv ut resultatet
vol1 = calculate_volume(5, 3, 2)
print(f"Volumet med lengde=5, bredde=3, høyde=2 er: {vol1}")

vol2 = calculate_volume(10, 4, 5)
print(f"Volumet med lengde=10, bredde=4, høyde=5 er: {vol2}")

vol3 = calculate_volume(7, 2, 8)
print(f"Volumet med lengde=7, bredde=2, høyde=8 er: {vol3}")