n1 = float(input('Qual a nota da p1? '))
n2 = float(input('Qual a nota da p2? '))
media = (n1 + n2)/2
print('O valor da sua média é {}'.format(media))
if media >= 7.0:
    print('Você está APROVADO!')
elif 4 <= media < 7:
    print('Você está em PROVA FINAL!')
else:
    print('Você está REPROVADO!')