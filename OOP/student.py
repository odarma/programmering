import random

class Student:
    '''klassen Student'''
    def __init__(self, fornavn, etternavn, alder, student_id):
        '''init, kjøres automatisk ved opprettelse av et objekt av denne klassen
        :param fornavn: fornavn (str)
        :param etternavn: etternavn (str)
        :param alder: alder (int)
        param student_id: id (int)'''
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.alder = alder
        self.student_id = student_id
        self.kurs = []
    
    def få_hele_navn(self):
        '''få tak i studentens fulle navn
        :return: fornavn etternavn (str)'''
        return f"{self.fornavn} {self.etternavn}: {self.alder} år\nID: {self.student_id}"
    
    def delta_i_kurs(self,kurs):
        self.kurs.append(kurs)

    def total_studiepoeng (self):
        total_studiepoeng = 0
        for kurs in self.kurs:
            total_studiepoeng += kurs.studiepoeng
        return total_studiepoeng


class Kurs:
    def __init__(self, navn, kode, studiepoeng):
        self.navn=navn
        self.kode=kode
        self.studiepoeng=studiepoeng

#person=Student(input("fornavn?\n"), input("etternavn?\n"), input("alder?\n"), random.randrange(0,1000000))
person=Student("nils", "nilsen", 23, random.randrange(0, 1000000))

print(person.få_hele_navn())