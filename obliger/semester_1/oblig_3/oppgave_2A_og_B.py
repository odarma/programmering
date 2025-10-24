import random

def tilfeldig_tall():
    for x in range(3):
        x=random.randrange(0,100) 
        print(f"tallet ble:", x)
    return x
tilfeldig_tall()

print("\nkoden under er laget av GPT UiO\n")

import random

def print_random_number():
    # Generer et tilfeldig tall mellom 0 og 100
    random_number = random.randrange(0, 101)
    # Lag en fin utskrift av tallet
    print(f"Det tilfeldig genererte tallet er: {random_number}")

# Kall funksjonen flere ganger
print_random_number()
print_random_number()
print_random_number()