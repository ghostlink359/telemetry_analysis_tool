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

def radRpm(rad):
    return rad * (60 / 2 * math.pi)