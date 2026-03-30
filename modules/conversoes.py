import math

def kmhToMs(vel):
    print(vel, ' em M/s: ', vel / 3.6)

def msToKmh(vel):
    print(vel, ' em Km/h: ', vel * 3.6)

def grausRad(n):
    print(n, ' em Rad: ', n * math.pi / 180)

def radGraus(n):
    print(n, ' em Graus: ', n * 180 / math.pi)

def rpmRad(rpm):
    print(rpm, ' em rad/s: ', rpm * (2 * math.pi / 60))

def rpmRad(rad):
    print(rad, ' em RPM: ', rad * (60 / 2 * math.pi))

def metroKm(m):
    print(m, ' em Km: ', m / 1000)

def kmMetro(km):
    print(km, ' em m: ', km * 1000)

def segMin(s):
    print(s, ' em minutos: ', s / 60)

def minSeg(min):
    print(min, ' em segundos: ', min * 60)

def nToKn(n):
    print(n, ' em kN: ', n / 1000)

def knToN(kn):
    print(kn, ' em N: ', kn * 1000)

def jToKj(j):
    print(j, ' em kJ: ', j / 1000)

def kjToJ(kj):
    print(kj, ' em J: ', kj * 1000)

