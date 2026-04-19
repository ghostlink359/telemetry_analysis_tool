def ler_lista(msg):
    while True:
        try:
            entrada = input(msg)
            return list(map(float, entrada.split(',')))
        except:
            print("Invalid Format! Use: 10,20,30")