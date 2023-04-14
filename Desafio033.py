a = int(input('Digite um primeiro número inteiro: '))
b = int(input('Digite um segundo número inteiro: '))
c = int(input('Digite um terceiro número inteiro: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor número escolhido entre os três é: {}'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior número escolhido entre os três é: {}'.format(maior))
