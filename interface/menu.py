from core.physics import velMedia, acel, forca, enerCin, drag 
from core.conversions import kmhToMs, msToKmh, grausRad, radGraus, rpmRad, radRpm

def telemetryMenu(n):
    while True:
        print('=== TELEMETRIA ===')

        print ('SELECIONE UMA OPÇÃO:')
        print ('1 - Inserir Dados')
        print ('2 - Análise Básica')
        print ('3 - Detectar Eventos')
        print ('4 - Comparar Voltas')
        print ('5 - Gráfico')
        print ('0 - Voltar')
        escolhaTele = input('Insira sua escolha: ')

        match escolhaTele:
            case '1':
                print('teste')
            case '0':
                break
            case _:
                print('Insira uma opção válida!')
                

def menuPhys(n):
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
                result = velMedia(float(d), float(t))
                print('Resultado: ', result)
            case '2':
                vi = input('Insira o valor da velocidade inicial (em metros): ')
                vf = input('Insira o valor do velocidade final (em metros): ')
                t = input('Insira o intervalo de tempo (em segundos): ')
                result = acel(float(vi), float(vf), float(t))
                print('Resultado: ', result)
            case '3':
                m = input('Insira o valor da massa (em kg): ')
                a = input('Insira o valor da aceleração (em m/s²): ')
                result = forca(float(m), float(a))
                print('Resultado: ', result)
            case '4':
                m = input('Insira o valor da massa (em kg): ')
                v = input('Insira o valor do velocidade (em m/s): ')
                result = enerCin(float(m), float(v))
                print('Resultado: ', result)
            case '5':
                p = input('Insira o valor da densindade do ar (em kg/m³): ')
                v = input('Insira o valor do velocidade (em m/s): ')
                cd = input('Insira o valod do coeficiente de arrasto: ')
                a = input('Insira o valor da área (em m²): ')
                result = drag(float(p), float(v), float(cd), float(a))
                print('Resultado: ', result)
            case '0':
                break
            case _:
                print('Escolha uma opção válida!')

def menuTools(n):
    while True:
        print('=== CONVERSÕES ===')

        print ('SELECIONE UMA OPÇÃO:')
        print ('1 - Velocidade')
        print ('2 - Ângulo')
        print ('3 - Rotação')
        print ('0 - Voltar')
        escolhaConv = input('Insira sua escolha: ') 

        match escolhaConv:
            case '1':
                vel = input('Insira a velocidade: ')
                result = kmhToMs(float(vel))
            case '0':
                break
            case _ :
                print('Insira uma escolha válida!')

