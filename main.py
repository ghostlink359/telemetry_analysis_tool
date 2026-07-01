import pandas as pd

df = pd.read_csv(r'C:\Users\908430\Desktop\calculadoraCient\telemetry_calc\files\formulaOneLaps.csv')

while True:
    print('=== TELEMETRY SYSTEM ===')

    print ('Choose an Option:')
    print ("1 - Teste Planilha")
    print ('0 - Leave')
    escolha = input('Choose your option: ')

    match escolha:
        case '1':
            print(df.head(25))
        case '0':
            print('Leaving the System...')
            break
        case _:
            print ('Choose a valid option!')
