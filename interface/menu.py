from core.math_ops import media
from core.physics import velMedia, acel, forca, enerCin, drag
from core.conversions import kmhToMs, grausRad, rpmRad
from interface.input_handler import ler_lista
import matplotlib.pyplot as plt

def telemetryMenu():
    while True:
        print('=== TELEMETRY ===')

        print('CHOOSE AN OPTION:')
        print('1 - Insert Data')
        print('2 - Basic Analysis')
        print('3 - Compare Laps')
        print('4 - Graph')
        print('0 - Go Back')
        escolhaTele = input('Choose an option: ')

        match escolhaTele:
            case '1':
                list1 = ler_lista('Enter speeds (km/h) separated by commas: ')
            case '2':
                if list1 is None:
                    print("Insert data first!")
                    continue
                result = media(list1)
                print('Average speed:', result)
                result = max(list1)
                print('Maximum speed:', result)
                result = min(list1)
                print('Minimum speed:', result)
            case '3':
                list2 = ler_lista('Enter speeds (km/h) separated by commas: ')
                for i in range(min(len(list1), len(list2))):
                    print(f"Point {i}: {list1[i] - list2[i]}")
            case '4':
                plt.plot(list1)
                plt.title("Speed vs Time")
                plt.xlabel("Time")
                plt.ylabel("Speed (km/h)")
                plt.grid()
                plt.show()
            case '0':
                break
            case _:
                print('Enter a valid option!')              

def menuPhys():
    while True:
        print('=== PHYSICS CALCULATOR ===')

        print('CHOOSE AN OPTION:')
        print('1 - Average Speed')
        print('2 - Acceleration')
        print('3 - Force')
        print('4 - Kinetic Energy')
        print('5 - Aerodynamic Drag')
        print('0 - Go Back')
        escolhaFisica = input('Choose an option: ')

        match escolhaFisica:
            case '1':
                d = input('Enter distance: ')
                t = input('Enter time: ')
                result = velMedia(float(d), float(t))
                print('Result:', result)
            case '2':
                vi = input('Enter initial velocity (m/s): ')
                vf = input('Enter final velocity (m/s): ')
                t = input('Enter time interval (s): ')
                result = acel(float(vi), float(vf), float(t))
                print('Result:', result)
            case '3':
                m = input('Enter mass (kg): ')
                a = input('Enter acceleration (m/s²): ')
                result = forca(float(m), float(a))
                print('Result:', result)
            case '4':
                m = input('Enter mass (kg): ')
                v = input('Enter velocity (m/s): ')
                result = enerCin(float(m), float(v))
                print('Result:', result)
            case '5':
                p = input('Enter air density (kg/m³): ')
                v = input('Enter velocity (m/s): ')
                cd = input('Enter drag coefficient: ')
                a = input('Enter area (m²): ')
                result = drag(float(p), float(v), float(cd), float(a))
                print('Result:', result)
            case '0':
                break
            case _:
                print('Enter a valid option!')

def menuTools():
    while True:
        print('=== CONVERSIONS ===')

        print('CHOOSE AN OPTION:')
        print('1 - Speed (km/h -> m/s)')
        print('2 - Angle (degrees -> radians)')
        print('3 - Rotation (RPM -> rad/s)')
        print('0 - Go Back')
        escolhaConv = input('Choose an option: ')

        match escolhaConv:
            case '1':
                vel = input('Enter speed: ')
                result = kmhToMs(float(vel))
                print('Result:', result)
            case '2':
                ang = input('Enter angle: ')
                result = grausRad(float(ang))
                print('Result:', result)
            case '3':
                rpm = input('Enter RPM: ')
                result = rpmRad(float(rpm))
                print('Result:', result)
            case '0':
                break
            case _:
                print('Enter a valid option!')