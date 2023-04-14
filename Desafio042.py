r1 = float(input('Qual o comprimento da primeira reta? '))
r2 = float(input('Qual o comprimento da segunda reta? '))
r3 = float(input('Qual o comprimento da terceira reta? '))

a = r1 + r2
b = r1 + r3
c = r2 + r3
if a > r3:
    a = 1
if b > r2:
    b = 1
if c > r1:
    c = 1
if a + b + c == 3:
    print('Poderemos formar uma triângulo com esses 3 valores')
else:
    print('Não poderemos formar um triângulo com esses 3 valores')
if r1 == r2 == r3:
    print('E o triângulo formado é um triângulo equilátero')
elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
    print('E o triângulo formado é um triângulo isósceles')
else:
    print('E o triângulo formado é um triângulo escaleno')
