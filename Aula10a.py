#nome = str(input('Qual o seu nome? '))
#if nome == 'Tayan':
#    print('Seu nome é lindo')
#else:
#    print('Seu nome é normal!')
#print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a nota da p1 '))
n2 = float(input('Digite a nota da p2 '))
n = (n1 + n2)/2
print('A média da sua nota é: {}'.format(n))
if n >= 7.0:
    print('Você está aprovado')
else:
    print('Você está em Prova Final')