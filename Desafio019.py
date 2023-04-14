import random as rd
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]
sorteado = rd.choice(alunos)
print('O aluno que irá apagar o quadro será: {}'.format(sorteado))

#print('O sorteado entre João, Kleber, Wilson e Vinicius, que irá apagar o quadro será: {}'.format(rd.choice(['João', 'Kleber', 'Wilson', 'Vinicius'])))