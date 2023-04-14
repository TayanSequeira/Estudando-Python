#int = numero inteiro
#float = numero real
#bool = true ou false
#str = string, escrever sempre entre aspas
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
s = n1 + n2
#print('A soma entre ', n1, 'e', n2, "vale ", s) > sintaxe antiga
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s)) #Sintaxe nova


