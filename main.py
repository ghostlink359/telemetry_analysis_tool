from interface.menu import telemetryMenu, menuPhys, menuTools

import pandas as pd

df = pd.read_csv('formulaOneLaps.csv')

while True:
    print('=== TELEMETRY SYSTEM ===')

    print ('Choose an Option:')
    print ('1 - Telemetry')
    print ('2 - Physics')
    print ('3 - Tools')
    print ('0 - Leave')
    escolha = input('Choose your option: ')

    match escolha:
        case '1':
            telemetryMenu()
        case '2':
            menuPhys()
        case '3':
            menuTools()
        case '4':
            print(df.head())
        case '0':
            print('Leaving the System...')
            break
        case _:
            print ('Choose a valid option!')
