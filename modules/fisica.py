def velMedia (d, t):
    print ('A velocidade média é de: ', d / t, ' m/s, ou ', (d / t) * 3.6, ' Km/h' )

def acel (vi, vf, t):
    print('A aceleração é de: ', (vf - vi) / t, ' m/s²')

def forca (m, a):
    print ('A força é de : ', m * a, ' N')

def enerCin (m, v):
    print ('A energia cinética é de: ', 1/2 * m * (v ** 2), ' J')

def drag (p, v, cd, a):
    print ('O Arrasto é de: ', 0.5 * p * (v ** 2) * cd * a, 'N')