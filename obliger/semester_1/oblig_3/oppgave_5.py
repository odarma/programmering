film = [ #dictionary i liste
    {"navn":"inception","år":2010,"vurdering":8.7},

    {"navn":"inside out","år":2015,"vurdering":8.1},

    {"navn":"con air", "år":1997,"vurdering":6.9}
]
#notat til de som vurderer koden:
#ha terminalen på fullskjerm eller delvis utvidet
#jeg valgte å kombinere deloppgavene til en hel kode og fil for enkelhets skyld
#framover vil liste-variabelen være film-listen over, og verdi-variabelen er values-verdiene i keys:values-paret i dictionary-ene
#husk å skrive med små bokstaver

def innlagt_filmer(navn, år, vurdering): #legger inn input-ene som dictionary i liste
    film.append({"navn":navn, "år":år, "vurdering":vurdering})
    return

def print_list(liste): #skrive ut listen i den gitte formatet
    for verdi in liste:
        print(f'\n{verdi["navn"]} - {verdi["år"]} has a rating of {verdi["vurdering"]}')
    return

def gjennomsnitt(liste): #regne gjennomsnitt
    total_rating=0
    for verdi in liste:
        total_rating+=verdi["vurdering"]
    gjennomsnitt_ut= total_rating/len(verdi)
    print(f'gjennomsnittet er {round(gjennomsnitt_ut,1)}')
    print(f'\ntotal rating er {round(total_rating,1)}')
    return 

def filtrering(liste,år):#filtrerer og skriver ut informasjon om film etter 2010
    filter_liste=[]
    for verdi in liste:
        if verdi["år"]>=år:
            filter_liste.append(verdi)
    for verdi in filter_liste:
        print(f'\n{verdi["navn"]} - {verdi["år"]} has a rating of {verdi["vurdering"]}\n')
    return

def skrive_til_fil(liste,fil):
    with open(fil, 'w') as file:
        for verdi in liste:
            file.write(f'{verdi["navn"]} - {verdi["år"]} has a rating of {verdi["vurdering"]}\n')
    return

def lese_av_fil(fil):
    with open(fil, 'r') as file:
        innhold = file.read()
        print(innhold)
    return

while True: #velge handling
    valg=input("\n---------------------------"
    "\n-----hva vil du gjøre?-----\n" \
    "---------------------------"
    "\nlegge inn film (1)\n" \
    "se gjennomsnittsratingen (2)\n" \
    "filtrer (3)\n" \
    "lese av fil (4)\n" \
    "avslutte (5)\n" \
    "\nskriv her:")  
    if valg == "1":  #valgte å ikke hardkode filmene, utgivelsesår og rating
        while True:    
            navn_inn=input("\nhvilke film skal med i listen?")
            år_inn=int(input("når ble den utgitt?"))
            try: #måtte skrive denne koden fordi jeg hadde problemer når vurdering_inn har ingen verdi
                vurdering_inn=float(input("hvor mange stjerner av 10 fikk filmen?"))
            except ValueError: #hvis variabelen får en rating-verdi vil "except ValueError" bli hoppet over
                vurdering_inn=5.0
            innlagt_filmer(navn_inn,år_inn,vurdering_inn)
            skrive_til_fil(film,"movies.txt") #skriver eksisterende og innlagt verdier til filen

            #teknisk sett blir kravet "Benytt funksjonen til å legge til 3 filmer du selv bestemmer." fylt ved å skrive inn 3 filmer
            svar=input("vil du legge inn flere filmer?\nja/nei\nskriv her:") 
            if svar == "ja":
                print("disse filmene er i listen:\n")
                print_list(film)
                continue
            elif svar=="nei":
                print("ok her er filmene du la inn:\n")
                print_list(film)
                break #tar deg til starten av while-løkken

    elif valg=="2": #printer ut gjennomsnittsratingen og totalratingen
        gjennomsnitt(film)

    elif valg=="3":
        filter_år=2010
        filtrering(film,filter_år)

    elif valg=="4":
        lese_av_fil("movies.txt")

    elif valg =="5": #avslutter programmen
        break