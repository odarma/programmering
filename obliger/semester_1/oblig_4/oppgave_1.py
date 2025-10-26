class Film: #koden gjelder deloppgave A og B 
    def __init__(self, tittel, utgivelsesår, vurdering):
        self.tittel = tittel
        self.utgivelsesår = utgivelsesår
        self.vurdering = vurdering
    def skriv_ut(self):
        return f'{self.tittel} ble utgitt i {self.utgivelsesår} og har {self.vurdering} av 10 stjerner\n'

film_1=Film("inception", 2010, 8.8)
film_2=Film("the martian", 2015, 8.4)
film_3=Film("joker", 2019, 8.4)

print(film_1.skriv_ut())
print(film_2.skriv_ut())
print(film_3.skriv_ut())