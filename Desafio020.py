import random as rd
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]
rd.shuffle(alunos)
print('A ordem dos alunos que iram apresentar será: {}'.format(alunos))



#alunos = 'Jorge Aline Fernanda Gabriel'.split()
#rd.shuffle(alunos)
#print('A ordem dos alunos que iram apresentar será: {}'.format(alunos))