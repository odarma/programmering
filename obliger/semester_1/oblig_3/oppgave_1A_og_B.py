student = { 
    "first name" : "Ola", 
    "last name" : "Nordmann",
    "favourite course" : "Programmering 1" 
} 
student["favourite course"] = "ITF10219 Programmering 1"
student["age"] = 19

print (f"first name:",student["first name"],"\nlast name:",student["last name"], 
       "\nfavorite course: ", student["favourite course"], "\nage: ", student["age"])

print("\nkoden under er laget av GPT UiO\n")

# Opprinnelig dictionary
student = {
    "first name": "Ola",
    "last name": "Nordmann",
    "favourite course": "Programmering 1"
}

# 1. Skriv ut studentens fullstendige navn
full_name = student["first name"] + " " + student["last name"]
print("Studentens fullstendige navn:", full_name)

# 2. Endre studentens favorittkurs til å inkludere kursets emnekode
student["favourite course"] = "ITF10219 Programmering 1"

# 3. Legg til en alder for studenten
student["age"] = 21  # Du kan velge en annen alder om ønskelig

# Print ut den oppdaterte dictionarien
print("Oppdatert studentinfo:", student)