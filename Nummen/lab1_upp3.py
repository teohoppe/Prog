import numpy as np
import matplotlib.pyplot as plt
# a) 0 b)

gränser = [0, 2]
n = 4

def f(x):
    return x**3*np.exp(x)

def trapets(antal_I, bounds, func):
    h = (bounds[1] - bounds[0]) / antal_I
    Th = []
    x = np.arange(bounds[0], bounds[1] + h, h)

    f_values = func(x)
    Th.append(h * (np.sum(f_values) - 0.5 * (f_values[0] + f_values[-1])))
    print(f'Integralresultat med initiala steglängden (h={h}): {Th[0]}')

    for i in range(10):
        h /= 2
        x = np.arange(bounds[0], bounds[1] + h, h)
        f_values = func(x) 
        Th.append(h * (np.sum(f_values) - 0.5 * (f_values[0] + f_values[-1])))

    print('')
    print('Sista integralvärdet efter 10 steglängdshalveringar:',Th[-1])

    #Kolla konvergensordningen (kvoter)
    quotientT = np.divide(np.subtract(Th[1:-1],Th[:-2]),np.subtract(Th[2:],Th[1:-1]))
    print('')
    print('Konvergenskvoter:')
    print(quotientT)
    error = np.abs(Th[-1] - Th[-2])
    print(error)

    pS = np.log(quotientT)/np.log(2)
    print('')
    print(f'Den beräknade noggrannhetsordningen för Trapetsregeln blir {pS}')
    # The theoretical order is 2 which we can see it approaches

    return Th[-1]

#print(trapets(n, gränser, f))

# c)
def trapets2():
    h = 1

    f_values = np.array([12, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56])
    Th = (h * (np.sum(f_values) - 0.5 * (f_values[0] + f_values[-1])))
    print(Th)
    
    return Th

#trapets2()

# d)
def trapets3():
    h = 1
    Th = []
    for i in range(1, 9):
        print(i)
        f_values = np.array([12, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56])
        sampled = f_values[::i]
        h_eff = h * i
        Th.append(h_eff * (np.sum(sampled) - 0.5 * (sampled[0] + sampled[-1])))
        print(Th)

    print('')
    error1 = np.abs(Th[0] - Th[1])
    print(error1)
    error = np.abs(Th[1] - Th[3])
    print(error1/error)
    p = np.log(error/error1)/np.log(2)
    print(f'Den beräknade noggrannhetsordningen för Trapetsregeln blir {p}')
    
    return Th, p
#trapets3()

# e)
def richardson_extrapolation():
    """Richardson extrapolation using the two most accurate estimates from trapets3"""
    Th, p = trapets3()
    
    # Using the two finest step sizes (most accurate): Th[-2] and Th[-1]
    p_order = p  # Trapezoidal rule has order 2
    T_richardson = (2**p_order * Th[0] - Th[1]) / (2**p_order - 1)
    print(f'\nRichardson extrapolation: {T_richardson}')

    return T_richardson


def simpsons_rule():
    h = 1
    f_values = np.array([12, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56])
    Sh = (h/3) * (f_values[0] + 4 * np.sum(f_values[1:-1:2]) + 2 * np.sum(f_values[2:-2:2]) + f_values[-1])
    print(f'Simpsons regel resultat: {Sh}')

    return Sh


richardson_extrapolation()
simpsons_rule()
