#import planet_funksjoner as pf
from planet_funksjoner import *

# Variabelen run skal styre while-løkka. Så lenge run er True vil løkka gå om igjen og om igjen

run = True
while run:      # betyr det samme som while run == True
    # " PSEUDOKODE"
    #Skrive ut overskrift
        # Vi kaller funksjonen skriv_header(). Da utføres koden til den funksjonen, slik vi definerte den tidligere
    skriv_header()
    #Skrive ut liste over planeter
        # Vi kaller funksjonen skriv_ut_planetliste(planeter) og sender med lista vår 'planeter' som argument. Da utføres koden til den funksjonen, slik vi definerte den tidligere
    skriv_ut_planetliste(planeter)
    #Ta input med valg, og en tilbakemelding
    planetnummer = int(input("\n Velg en planet ved å skrive inn et tall: "))
    # Evt velge tilfeldig, og tilbakemelding
        # Dersom brukeren har valgt 0 for tilfeldig planet kaller vi funksjonen velg_tilfeldig() for å trekke et tall.        
    if planetnummer == 0:
        valgt_planet = velg_tilfeldig(planeter)      # Denne variabelen vil få datatypen dict, siden funksjonen vi definerte returnerer en dict fra den gitte indeksen i lista
        print(f"Du fikk planeten {valgt_planet['navn']}")
    # Ellers bruker vi tallet brukeren valgte som indeks for å finne planeten i lista vår  
    else:
        valgt_planet = planeter[planetnummer]        # Denne variabelen vil få datatypen dict, siden funksjonen vi definerte returnerer en dict fra den gitte indeksen i lista
        print(f"Du har valgt planeten {valgt_planet['navn']}")

    # Ta input med vekt, gjør den direkte om til float
    brukervekt = float(input("Hva er din vekt på jorden?: "))

    #Beregninger
    # beregner den nye veklten med funksjonen vi definerte og lagrer det i en variabel. Argumentene vi sender med er vekten som ble skrevet inn og tyngdekraften på den valgte planeten
    vekt_pa_annen_planet = beregn_vekt(brukervekt, valgt_planet['tyngdekraft'])
    
    #Tilbakemelding
    print(f"Din vekt på planeten {valgt_planet['navn']} med tyngdekraft {valgt_planet['tyngdekraft']} er {vekt_pa_annen_planet} kg")

    #Ta input om avslutning
    # run skal som nevnt styre løkka, her vil verdien til run (True/False) bli bestemt av hva som returneres fra funksjonen vår en_gang_til.
    run = en_gang_til()