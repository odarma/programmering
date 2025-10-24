#Dette er 'programmet' vårt. Vi importerer modulen vi laget, jsonmodul.py, og bruker funksjonene vi definerte der.

import json_modul


#Lager en dictionary, som vi ønsker å skrive til en json-fil senere
planet = {"navn" : "Merkur", "tyngdekraft" : 3.73}

#Lagrer filnavnet vi ønsker å bruke i en variabel
file_name = "planet.json"

#Brukerskriv_json()-funksjonen vi definerte i vår jsonmodul, og sender med variablene vi akkurat opprettt som argumenter
#Vi får nå opprettet en ny fil med navnet planet.json, og som inneholder en string med vår dictionary 
json_modul.skriv_json(planet, file_name)

dictionary_from_file=json_modul.les_json(file_name)
print(dictionary_from_file)
print(type(dictionary_from_file))

print(dictionary_from_file['navn'])