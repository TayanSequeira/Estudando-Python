frase = str(input('Digite um frase qualquer: ')).upper().strip()
print('Quantidade de (a), que existe na frase: ', frase.count('A'))
print('Localização do primeiro (a) na frase: ', frase.find('A')+1)
print('A última letra A aparece na posição', frase.rfind('A')+1)