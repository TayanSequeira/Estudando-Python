#MANIPULANDO CADEIA DE TEXTO
# Quando trabalhamos com Range nunca é pego o ultimo valor.
# para separar em range, podemos escollher a variavel
# ex: frase[9:21:2]
#[LETRA ESCOLHIDA:ATÉ ONDE VAI (-1):PULANDO DE DOIS EM DOIS]
#[:5], COMO SE FOSSE ZERO ATÉ LETRA 4
#[15:], QUERO DO 15 ATÉ O FINAL
#[9::3], vai começar no 9 o segundo numero como nao tem nada, vai até o final, pulando de 3 em 3 pua o 9, 10 e 11 e vai mostrar o numero 12...
# frase.count('o'), vai contar a quantidade de letras 'o' existem numa frase
# frase.count('o',0,13) vai fazer a contagem da letra 'o', no intervalo de [0,13[
# frase.find('deo') quantas vezes ele encontrou o 'deo', vai dizerr aonde começou a palavra 'deo'
# CASO A STRING NAO EXISTA O PYTHON VAI ME RESPONDER -1, PORQUE ELE NAO EXISTE
# frase.replace('Python','Android') = isso vai substituir a string python pela string android
# frase.upper() = deixar as letras em maíusculo
# frase.lower() = deixa tudo em minúsculo
# frase.capitalize() = jogar todos os caracteres para minusculo e apenas o primeiro ficará em maisculo(FORMATAÇÃO)
# frase.title() = vai analisar quantas palavras tem a frase, e vai deixar todas as primeiras letras de cada palavra em maiusculo
# frase.strip() = remove os espaços inúteis, remove os espaços antes e no final da frase
# frase.rstrip() = remove apenas os espaços do lado direito, no caso os ultimos
# frase.lstrip() = remove apenas os espaços do lado esquerdo, no caso os primeiros
# frase.split() = cada palavra vai ser separada em uma outra lista
# ex: Curso   em video Python
#     012345  01 01234 012345
#'-'.join(frase) = irá colocar um traço entre as palavras