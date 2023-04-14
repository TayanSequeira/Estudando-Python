r1 = float(input('Digite o valor de um segmento de reta: '))
r2 = float(input('Digite outro valor de um segmento de reta: '))
r3 = float(input('Digite outro valor de um segmento de reta: '))
#arrumando os valores
a = r1 + r2
b = r1 + r3
c = r2 + r3
if a > r3:
    a = 1
if b > r2:
    b = 1
if c > r1:
    c = 1
if a + b + c ==3:
    print('Poderemos formar uma triângulo com esses 3 valores')
else:
    print('Não poderemos formar um triângulo com esses 3 valores')

