ny_liste=[] 
ny_liste2=[]
liste=[
    "The Hobbit", 
    "Farmer Giles of Ham",  
    "Lord of the Rings: The Fellowship of the Ring", 
    "Lord of the Rings: The Two Towers", 
    "Lord of the Rings: The Return of the King", 
    "The Adventures of Tom Bombadil",  
    "Tree and Leaf"]
for i in liste:
    if "Lord of the Rings: " in i:
        ny_liste.append(i)
print(ny_liste)

for i in liste:
    if len(i)>=32:
        ny_liste2.append(i)
print(ny_liste2)