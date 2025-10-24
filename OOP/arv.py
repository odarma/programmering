class Dyr:
    def __init__(self, navn, alder):
        self.navn=navn
        self.alder=alder
    
    def få_navn(self):
        return self.navn

class Honey_badger(Dyr):
    def __init__(self, navn, alder, sgiven=0):
        super().__init__(navn, alder)
        self.sgiven=sgiven 

dyr_1=Honey_badger("nils-christian",3,0)
dyr_2=Dyr("anne", 4)

print(dyr_1.navn)
print(dyr_1.få_navn())
print(dyr_1.sgiven)
print(dyr_2.sgiven)