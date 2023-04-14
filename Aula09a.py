frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[1:14])
print(frase[:])
print(frase[:6])
print(frase[:16:3])
print(frase[3:13:4])
print(frase[::3])

print('Oi')
print("""Vamos supor que eu queira escrever um texto
muito grande, em que iria dar muito trabalho 
colocar o print no começo de cada linha, oq
eu posso fazer e colocar print e 3 aspas""")

print(frase.count('o'))
print(frase.upper().count('O'))
print(frase.strip())
print(len(frase.strip()))
print(frase.replace('Python','Tayan'))
print(frase)
#frase = print(frase.replace('Python','Tayan')) #aqui estou fazendo atribuição a variavel frase
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.find('video'))
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
print(dividido[0])