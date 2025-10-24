import random

def dart_game(): 
    total_poeng=0
    print("velkommen til dart-spillet. hvor mange spillere skal med?")
    spillere=int(input("skriv her:"))

    while True:
        for spiller in range(spillere):  
            for _ in range(3):
                poeng=random.randrange(0,60)
                total_poeng+=poeng
                print(f"spiller {spiller} fikk {poeng} poeng dette kastet.")
            print(f"spiller {spiller} fikk totalt {total_poeng} poeng")    
            
        return total_poeng        

dart_game()