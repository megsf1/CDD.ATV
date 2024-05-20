from classes import *

p1 = Pessoa("Jõao",75,35)
p2 = Pessoa("Maria",55,23)
print(f'Nome: {p1.nome} , Peso: {p1.peso} , Idade: {p1.idade}')
p2.peso = 60

print(f'Nome: {p2.nome} , Peso: {p2.peso} , Idade: {p2.idade}.')


p1.comer("maçã")
p1.pararcomer()
p1.andar()
p1.pararAndar()
p1.falar()
p1.pararfalar()
p1.comer("banana")
p2.comer("feijão")


