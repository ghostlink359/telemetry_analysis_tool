from interface.menu import telemetryMenu, menuPhys, menuTools

while True:
    print('=== CALCULADORA DE TELEMETRIA ===')

    print ('SELECIONE UMA OPÇÃO:')
    print ('1 - Telemetria')
    print ('2 - Física Aplicada')
    print ('3 - Ferramentas')
    print ('0 - Sair')
    escolha = input('Insira sua escolha: ')

    match escolha:
        case '1':
            telemetryMenu()
        case '2':
            menuPhys()
        case '3':
            menuTools()
        case '0':
            print('Encerrando sistema...')
            break
        case _:
            print ('Escolha uma opção valida!')
