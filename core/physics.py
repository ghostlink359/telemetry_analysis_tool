def velMedia (d, t):
    return  d / t

def acel (vi, vf, t):
    return (vf - vi) / t

def forca (m, a):
    return m * a

def enerCin (m, v):
    return 1/2 * m * (v ** 2)

def drag (p, v, cd, a):
    return 0.5 * p * (v ** 2) * cd * a