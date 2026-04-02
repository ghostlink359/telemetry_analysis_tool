from core.math_ops import mult, div, pow, raiz, raizCub,tan, fat, exp 
from core.physics import velMedia, acel, forca, enerCin, drag 
from core.conversions import kmhToMs, msToKmh, grausRad, radGraus, rpmRad, metroKm, kmMetro, segMin, minSeg, nToKn, knToN, jToKj, kjToJ 

while True:
    print('=== CALCULADORA DE TELEMETRIA ===')

    print ('SELECIONE QUE TIPO DE CALCULO DESEJA REALIZAR:')
    print ('1 - Básicos')
    print ('2 - Científicos')
    print ('3 - Físicos')
    print ('4 - Conversões')
    print ('0 - Sair')
    escolha = input('Insira sua escolha: ')

    match escolha:
        case '1':
            while True:
                print('=== CALCULOS BÁSICOS ===')
                
                print ('SELECIONE UMA OPÇÃO:')
                print ('1 - Multiplicação')
                print ('2 - Divisão')
                print ('0 - Voltar')
                subEscolha = input('Insira sua escolha: ')  

                match subEscolha:
                    case '1':
                        n1 = input ('Insira o primeiro número: ')
                        n2 = input('Insira o segundo número: ')
                        mult(float(n1), float(n2))
                    case '2':
                        n1 = input ('Insira o primeiro número: ')
                        n2 = input('Insira o segundo número: ')
                        div(float(n1), float(n2)) 
                    case '0':
                        break
                    case _:
                        print ('Escolha uma opção valida!')
        case '2':
            while True:
                print('=== CALCULOS CIENTÍFICOS ===')

                print ('SELECIONE UMA OPÇÃO:')
                print ('1 - Potência')
                print ('2 - Raiz Quadrada')
                print ('3 - Raiz Cúbica')
                print ('4 - Tangente')
                print ('5 - Fat')
                print ('6 - Exponencial')
                print ('0 - Voltar')
                escolhaCient = input('Insira sua escolha: ') 

                match escolhaCient:
                    case '1':
                        n1 = input ('Insira a base: ')
                        n2 = input('Insira a potência: ')
                        pow(float(n1), float(n2))
                    case '2':
                        n1 = input ('Insira o número: ')
                        raiz(float(n1))
                    case '3':
                        n1 = input ('Insira o número: ')
                        raizCub(float(n1))
                    case '4':
                        n1 = input ('Insira o número: ')
                        tan(float(n1))
                    case '5':
                        n1 = input ('Insira o número: ')
                        fat(int(n1))
                    case '6':
                        n1 = input ('Insira o número: ')
                        exp(float(n1))  
                    case '0':
                        break
                    case _:
                        print ('Escolha uma opção valida!')
        case '3':
            while True:
                print('=== CALCULADORA FÍSICOS ===')

                print ('SELECIONE UMA OPÇÃO:')
                print ('1 - Velocidade Média')
                print ('2 - Aceleração')
                print ('3 - Força')
                print ('4 - Energia Cinética')
                print ('5 - Arrasto aerodinâmico')
                print ('0 - Voltar')
                escolhaFisica = input('Insira sua escolha: ') 

                match escolhaFisica:
                    case '1':
                        d = input('Insira o valor da distância: ')
                        t = input('Insira o valor do tempo: ')
                        velMedia(float(d), float(t))
                    case '2':
                        vi = input('Insira o valor da velocidade inicial (em metros): ')
                        vf = input('Insira o valor do velocidade final (em metros): ')
                        t = input('Insira o intervalo de tempo (em segundos): ')
                        acel(float(vi), float(vf), float(t))
                    case '3':
                        m = input('Insira o valor da massa (em kg): ')
                        a = input('Insira o valor da aceleração (em m/s²): ')
                        forca(float(m), float(a))
                    case '4':
                        m = input('Insira o valor da massa (em kg): ')
                        v = input('Insira o valor do velocidade (em m/s): ')
                        enerCin(float(m), float(v))
                    case '5':
                        p = input('Insira o valor da densindade do ar (em kg/m³): ')
                        v = input('Insira o valor do velocidade (em m/s): ')
                        cd = input('Insira o valod do coeficiente de arrasto: ')
                        a = input('Insira o valor da área (em m²): ')
                        drag(float(p), float(v), float(cd), float(a))
                    case '0':
                        break
                    case _:
                        print('Escolha uma opção válida!')
        case '4':
            print('=== CONVERSÕES ===')

            print ('SELECIONE UMA OPÇÃO:')
            print ('1 - Velocidade')
            print ('2 - Ângulo')
            print ('3 - Rotação')
            print ('4 - Distância')
            print ('5 - Tempo')
            print ('6 - Força')
            print ('7 - Energia')
            print ('0 - Voltar')
            escolhaConv = input('Insira sua escolha: ') 

            match escolhaConv:
                case '1':
                    print ('SELECIONE UMA OPÇÃO:')
                    print ('1 - Velocidade')
                    print ('2 - Ângulo')
                    print ('3 - Rotação')
                    print ('4 - Energia')
                    print ('0 - Voltar')
                    escolhaVel = input('Insira sua escolha: ')

                    match escolhaVel:    
                        case '1': 
                            vel = input('Insira a velocidade: ')
                            kmhToMs(float(vel))
                        case '2':
                            vel = input('Insira a velocidade: ')
                            msToKmh(float(vel))
                        case '0':
                            break
                        case _ :
                            print('Insira uma escolha válida!')
        case '0':
            print('Encerrando sistema...')
            break
        case _:
            print ('Escolha uma opção valida!')
