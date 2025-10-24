from student import Student, Kurs
import kurs_funksjoner
import random

#person=Student(input("fornavn?\n"), input("etternavn?\n"), input("alder?\n"), random.randrange(0,1000000))
person=Student("nils", "nilsen", 23, random.randrange(0, 1000000))

programmering_1=Kurs("programmering 1", "ITF10219", 10)
webutvikling = Kurs("webutvikling", "ITF12084", 10)
innføring = Kurs("innføring i design av digitale produkter", "ITF10346", 10)

person.delta_i_kurs(programmering_1)
person.delta_i_kurs(webutvikling)
person.delta_i_kurs(innføring)

print(type(person))
print(f"total antall studiepoeng med {person.total_studiepoeng}")
print(f"total antall studiepoeng med kurs-funksjon:\n{person.total_studiepoeng}")

alle_kurs=[programmering_1, webutvikling, innføring]
print(f"total antall studiepoeng fra liste utenfor en klasse:\n{kurs_funksjoner.regne_total_studiepoeng(alle_kurs)}")


#print(list.append.__doc__)
print(kurs_funksjoner.regne_total_studiepoeng.__doc__)
print(Student.__doc__)
print(Student.__init__.__doc__)