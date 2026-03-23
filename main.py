n1 = input ('Insira o primeiro número do calculo: ')
n2 = input('Insira o segundo número do calculo: ')

print ('SELECIONE UMA OPÇÃO:')
print ('1 - Adição')
print ('2 - Subtração')
print ('3 - Multiplicação')
print ('4 - Divisão')
escolha = input('Insira sua escolha: ')

match escolha:
    case '1':
        soma(int(n1), int(n2))
    case _:
        print ('Escolha uma opção valida!')