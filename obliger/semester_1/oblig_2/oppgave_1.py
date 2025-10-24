print("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall. Svar under.")
svar=int(input())

if svar == 42:
    print("Det stemmer, meningen med livet er 42!")
elif 30 < svar < 50:
    print("nærme, men feil")
else:
    print("FEIL!")
