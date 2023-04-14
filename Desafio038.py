n1 = int(input('Escreva o primeiro número inteiro: '))
n2 = int(input('Escreva o segundo número inteiro: '))
if n1 > n2:
    print('O número {} é maior que o número {}'.format(n1, n2))
elif n1 < n2:
    print('O número {} é maior que o número {}'.format(n2, n1))
else:
    print('Não existe número maior, os dois números são iguais')