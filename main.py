import math

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

print ('SELECIONE QUE TIPO DE CALCULO DESEJA REALIZAR:')
print ('1 - Básicos')
print ('2 - Círentíficos')
print ('3 - Físicos')
escolha = input('Insira sua escolha: ')

match escolha:
    case '1':
        print ('SELECIONE UMA OPÇÃO:')
        print ('1 - Adição')
        print ('2 - Subtração')
        print ('3 - Multiplicação')
        print ('4 - Divisão')
        print ('0 - Voltar')
        escolha = input('Insira sua escolha: ')  

        match escolha:
            case '1':
                n1 = input ('Insira o primeiro número do calculo: ')
                n2 = input('Insira o segundo número do calculo: ')
                soma(float(n1), float(n2))
            case '2':
                n1 = input ('Insira o primeiro número do calculo: ')
                n2 = input('Insira o segundo número do calculo: ')
                sub(float(n1), float(n2))
            case '3':
                n1 = input ('Insira o primeiro número do calculo: ')
                n2 = input('Insira o segundo número do calculo: ')
                mult(float(n1), float(n2))
            case '4':
                n1 = input ('Insira o primeiro número do calculo: ')
                n2 = input('Insira o segundo número do calculo: ')
                div(float(n1), float(n2)) 
            case '0':
                escolha = int(0)  
            case _:
                print ('Escolha uma opção valida!')
    case '2':
        print ('SELECIONE UMA OPÇÃO:')
        print ('1 - Potência')
        print ('2 - Raiz Quadrada')
        print ('3 - Seno')
        print ('4 - Cosseno')
        print ('5 - Tangente')
        print ('6 - Log')
        print ('0 - Voltar')
    case '3':
        print ('SELECIONE UMA OPÇÃO:')
        print ('1 - Velocidade Média')
        print ('2 - Aceleração')
        print ('3 - Força')
        print ('4 - Energia Cinética')
        print ('5 - Arrasto aerodinâmico')
        print ('0 - Voltar')
    case _:
        print ('Escolha uma opção valida!')
