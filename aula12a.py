nome = str(input('Qual é o seu nome? '))
if nome == "Tayan":
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Silvio' or nome == 'Maria':
    print('Seu nome é comum no Brasil!')
else:
    print('Seu nome é comum!')
print('Tenha um bom dia, {}!'.format(nome))