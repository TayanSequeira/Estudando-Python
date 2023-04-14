n1 = str(input('Digite o nome da sua cidade: ')).strip()
#print(n1.find('Santo'))
#print("""Se aparecer 0 significa que sua cidade tem Santo no nome,
#se aparecer -1 significa que sua cidade não tem santo no nome""")
print(n1[:5].upper() == 'SANTO')