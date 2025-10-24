def regne_total_studiepoeng(liste_med_kurs):
    '''funksjonen skal regne ut antall studiepoeng fra en hvilken som helst lite med kurs-objekter
    :param liste med kurs: en liste med objekter av klassen Kurs (list)
    :param return: antall studiepoeng totalt for kurs (int)'''
    total_studiepoeng=0
    for element in liste_med_kurs:
        total_studiepoeng += element.studiepoeng
    return total_studiepoeng