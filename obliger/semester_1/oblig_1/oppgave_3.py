import operator
import sys

#definere hvilke funksjon tegnene skal gjøre
ops={'+': operator.add,
     '-': operator.sub,
     '*': operator.mul,
     '//': operator.floordiv,
     '/': operator.truediv,
     '**': operator.pow,
     '%': operator.mod} #definere hvilke funksjon tegnene skal gjøre

print("hvilke tall 1 skal skrives? skriv under:")
input_1=float(input())

print("hvilke operatør skal skrives? skriv under:")
operatoer=input()

if not operatoer in ops:
    print('ugyldig operatør, avslutter')
    sys.exit(1)

print("hvilke tall 2 skal skrives? skriv under:")
input_2=float(input())

print('det blir', ops[operatoer](input_1,input_2)) #regne ut