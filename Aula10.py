#AULA 10 (Condições Simples e Compostas)
#if e else if (se e se não)
#EStutura:
#se carro.esquerda()
#   Comadno para guiar o carro caminho esquerdo
#senão
#   Coomando para guiar o carro para caminho direito
#observar a identaçao para leitura do coodigo
#if carro.esquerda():
#   bloco true
#else:
#   bloco false
#ex:
#tempo = int(input('Quantos anos tem seu carro ? '))
#if tempo <=3:
#    print('Seu carro é novo')
#else:
#    print('Carro velho')
#print('--Fim--')
#mesmo exemplo condição simplificada:
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo'if tempo <=3 else 'Carro velho')
print('--Fim--')