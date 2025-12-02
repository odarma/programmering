from datetime import datetime

#3.1
#navn=input("hva er din navn?")
#alder=int(input("hva er din alder?"))
#nåværende_år=datetime.now().year
#print(f'hei {navn}! du vil bli 100 år i {nåværende_år+(100-alder)}')

#3.2
#økt=int(input('hvor mange minutter varte økten?'))
#if økt<30:
#    print(f'din økt er kategorisert som: lett')
#elif økt=<60:
#    print(f'din økt er kategorisert som: moderat')
#else:
#    print(f'din økt er kategorisert som: intens')

#3.3
#total_varighet=0
#for x in range(7):
#    varighet=int(input(f'skriv inn øktens varighet for dag {x+1}: '))
#    total_varighet+=varighet
#gjennomsnitt=total_varighet/7
#print(f'total treningstid for denne uken: {total_varighet}\ngjennomsnitt daglig treningstid for denne uken: {round(gjennomsnitt,2)}')

#3.6
while True:
    #3.4
    forbrenningsfart = [{'løping':15},{'svømming':10},{'sykling':8}]
    def kalkuler_brente_kalorier(treningstype,varihet):
        kalorier_brent=0
        varihet
        for key,value in treningstype.items():
            kalorier_brent = value*varihet
        return kalorier_brent
    valg=int(input('hva trente du?\n1: løpte\n2: svømte\n3: sykla\nskriv tall her:'))
    varighet_inn=int(input('hvor lenge trente du?'))
    trening=forbrenningsfart[valg-1]
    print(f'du brente omtrent {kalkuler_brente_kalorier(trening,varighet_inn)} kalorier')

    #3.5
    def loggføring(treningstype,varihet,logg):
        varihet
        logg
        for key,value in treningstype.items():
            kalorier_brent = value*varihet
            logg.append({'aktivitet':key,'varihet':varihet,'kalorier brent':kalorier_brent})
        print(f'loggførte {key} for {varihet} minutter, brente omtrent {kalorier_brent} kalorier')
        return logg
    logg=[]
    print(loggføring(trening,varighet_inn,logg))

    #3.6
    def lagre_data(logg,filnavn='treningsdata.txt'):
        with open(filnavn, 'a') as f:
            for data in logg:
                f.write(f'{data['aktivitet']},{data['varihet']},{data['kalorier brent']}\n')
        print('dataene lagret i fil')
        return
    lagre_data(logg)

    omstart = input('vil du loggføre flere økter? (j/n)').lower
    if omstart == 'j':
        continue
    elif omstart == 'n':
        break