pakkeliste=[]
print("----------hei. hva vil du gjøre med pakkelisten?----------")
valg=input("innlegg: legge inn ting i listen\nfjern: fjerne ting fra listen\nvis: vise listen\navslutt: avslutt programmen\nskriv her:") 

while True:
    if valg == "innlegg":
        ting=input("hva skal legges inn i listen?\nskriv her: ")
        pakkeliste.append(ting)
        print(pakkeliste)
        valg=input("skal du legge inn mer?\nja/nei\n")
        
        if valg=="ja":
            print(f"ting inni listen:  {pakkeliste}")
            ting=input("hva skal legges inn?\nskriv her: ")
            pakkeliste.append(ting)
            print(pakkeliste)
            valg=input("skal du legge inn mer?\nja/nei\n")

        elif valg=="nei":
               valg=input("----------hva vil du gjøre med pakkelisten?----------\n" \
                "innlegg: legge inn ting i listen\n" \
                "fjern: fjerne ting fra listen\n" \
                "vis: vise listen\n" \
                "avslutt: avslutt programmen\n" \
                "skriv her:")
    
    elif valg == "fjern":
        print(f"ting inni listen:  {pakkeliste}")
        ting=input("hva skal fjernes?\nskriv her: ")

        if ting in pakkeliste:
            pakkeliste.remove(ting)
            print(pakkeliste)
            valg=input("skal du fjerne mer?\nja/nei\n")
        
        elif ting not in pakkeliste:
            print("det du skrev finnes ikke")
            valg=input("----------hva vil du gjøre med pakkelisten?----------\n" \
            "innlegg: legge inn ting i listen\n" \
            "fjern: fjerne ting fra listen\n" \
            "vis: vise listen\n" \
            "avslutt: avslutt programmen\n" \
            "skriv her:")
        
        if valg=="ja":
            print(f"ting inni listen:  {pakkeliste}")
            ting=input("hva skal fjernes?\nskriv her: ")
            if ting in pakkeliste:
                pakkeliste.pop(ting)
                print(pakkeliste)
                valg=input("skal du fjerne mer?\nja/nei\n")

        elif valg=="nei":
                valg=input("----------hva vil du gjøre med pakkelisten?----------\n" \
                "innlegg: legge inn ting i listen\n" \
                "fjern: fjerne ting fra listen\n" \
                "vis: vise listen\n" \
                "avslutt: avslutt programmen\n" \
                "skriv her:")

    elif valg=="vis":
        print(pakkeliste)
        valg=input("----------hva vil du gjøre med pakkelisten?----------\n" \
        "innlegg: legge inn ting i listen\n" \
        "fjern: fjerne ting fra listen\n" \
        "vis: vise listen\n" \
        "avslutt: avslutt programmen\n" \
        "skriv her:")
    
    elif valg == "avslutt":
        break