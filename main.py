import math

n1 = input ('Insira o primeiro número do calculo: ')
n2 = input('Insira o segundo número do calculo: ')

def soma (n1, n2):
    print('Resultado: ', n1 + n2)

def sub (n1, n2):
    print ('Resultado: ', n1 - n2)

def mult (n1, n2):
    print ('Resultado: ', n1 * n2)

def div (n1, n2):
    print ('Resultado: ', n1 / n2)

def pow (n1, n2):
    print ('Resultado: ', n1 ** n2)

def raiz(n1):
    print ('Resultado: ', math.sqrt(n1))

def raizCub(n1):
    print ('Resultado: ', math.cbrt(n1))

print ('SELECIONE UMA OPÇÃO:')
print ('1 - Adição')
print ('2 - Subtração')
print ('3 - Multiplicação')
print ('4 - Divisão')
escolha = input('Insira sua escolha: ')

match escolha:
    case '1':
        soma(float(n1), float(n2))
    case '2':
        sub(float(n1), float(n2))
    case '3':
        mult(float(n1), float(n2))
    case '4':
        raizCub(float(n1))   
    case _:
        print ('Escolha uma opção valida!')