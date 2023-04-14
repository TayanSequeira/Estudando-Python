import random as rd
import time as tm
a = 1
b = 6
m = rd.randint(a, b)
print('-=-'*24)
print('Eu irei rolar um dado de 6 lados tente advinhar o número que irá cair...')
print('-=-'*24)
h = int(input('Qual número caiu ?: '))
print('Jogando o dado...')
tm.sleep(2)
if h == m:
    print('Parabéns você escolheu o número rolado!')
else:
    print('Infelizmente você errou o número rolado!')
print('O número rolado foi igual a: {}'.format(m))
