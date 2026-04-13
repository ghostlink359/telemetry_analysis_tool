from core.math_ops import media
from core.physics import velMedia, acel, forca, enerCin, drag 
from core.conversions import kmhToMs, grausRad, rpmRad
from interface.input_handler import ler_lista
import matplotlib.pyplot as plt

def telemetryMenu():
    while True:
        print('=== TELEMETRIA ===')

        print ('SELECIONE UMA OPÇÃO:')
        print ('1 - Inserir Dados')
        print ('2 - Análise Básica')
        print ('3 - Comparar Voltas')
        print ('4 - Gráfico')
        print ('0 - Voltar')
        escolhaTele = input('Insira sua escolha: ')

        match escolhaTele:
            case '1':
                list1 = ler_lista('Insira velocidades (km/h) separadas por vírgula:: ')
            case '2':
                if list1 is None:
                    print("Insira dados primeiro!")
                    continue
                result = media(list1)
                print('A média de velocidade é: ', result)
                result = max(list1)
                print('A velocidade máxima foi de: ', result)
                result = min(list1)
                print('A menor velocidade foi de: ', result)
            case '3':
                list2 = ler_lista('Insira velocidades (km/h) separadas por vírgula:: ')
                for i in range(min(len(list1), len(list2))):
                    print(f"Ponto {i}: {list1[i] - list2[i]}")
            case '4':
                plt.plot(list1)
                plt.title("Velocidade x Tempo")
                plt.xlabel("Tempo")
                plt.ylabel("Velocidade (km/h)")
                plt.grid()
                plt.show()
            case '0':
                break
            case _:
                print('Insira uma opção válida!')               

def menuPhys():
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

def menuTools():
    while True:
        print('=== CONVERSÕES ===')

        print ('SELECIONE UMA OPÇÃO:')
        print ('1 - Velocidade (km/h -> m/s)')
        print ('2 - Ângulo (graus -> rad)')
        print ('3 - Rotação (rpm -< rad/s)')
        print ('0 - Voltar')
        escolhaConv = input('Insira sua escolha: ') 

        match escolhaConv:
            case '1':
                vel = input('Insira a velocidade: ')
                result = kmhToMs(float(vel))
                print('Resultado: ', result)
            case '2':
                ang = input('Insira o ângulo: ')
                result = grausRad(float(ang))
                print('Resultado: ', result)
            case '3':
                rpm = input('Insira o RPM: ')
                result = rpmRad(float(rpm))
                print('Resultado: ', result)
            case '0':
                break
            case _ :
                print('Insira uma escolha válida!')

