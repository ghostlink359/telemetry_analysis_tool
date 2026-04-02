import math

def kmhToMs(vel):
    return vel / 3.6

def msToKmh(vel):
    return vel * 3.6

def grausRad(n):
    return n * math.pi / 180

def radGraus(n):
    return n * 180 / math.pi

def rpmRad(rpm):
    return rpm * (2 * math.pi / 60)

def rpmRad(rad):
    return rad * (60 / 2 * math.pi)

def metroKm(m):
    return m / 1000

def kmMetro(km):
    return km * 1000

def segMin(s):
    return s / 60

def minSeg(min):
    return min * 60

def nToKn(n):
    return n / 1000

def knToN(kn):
    return kn * 1000

def jToKj(j):
    return j / 1000

def kjToJ(kj):
    return kj * 1000

