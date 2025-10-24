liste=[
    "The Hobbit", 
    "Farmer Giles of Ham",  
    "The Fellowship of the Ring", 
    "The Two Towers", 
    "The Return of the King", 
    "The Adventures of Tom Bombadil",  
    "Tree and Leaf"]

print(liste[0:2])
print(liste[5:7])

liste.append("The Silmarillion")
liste.append("Unfinished Tales")
print(liste)

liste[2:5] = ["Lord of the Rings: The Fellowship of the Ring", 
    "Lord of the Rings: The Two Towers", 
    "Lord of the Rings: The Return of the King"]
print(liste)