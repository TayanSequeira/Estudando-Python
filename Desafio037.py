numero = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:'
[ 1 ] Converter para \033[31mBínário\033[m 
[ 2 ] Converter para \033[34mOctal\033[m
[ 3 ] Converter para \033[35mHexadecial\033[m''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para \033[31mBínário\033[m é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para \033[34mOctal\033[m é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para \033[35mHexadecial\033[m é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('{} Opção inválida. Tente novamente.')