import numpy as np
import pandas as pd
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt


# Constants
Rfi = 1.76 * 10**-4
Rf0 = 1.76 * 10**-4
hs = 356
ht = 356
kw = 60
c = 0.389
St = 0.016
K1 = 0.249
n1 = 2.207

# Known values from the problem
Aex = 64.15
Q = 801368
Ds = 1.219
Tm = 29.6

# Uppgift 1

def f(d, Ds, Q, Tm):
    return (Q / Tm) * ((d / (Ds*ht)) + d*Rfi/Ds + d*np.log(d/Ds)/(2*kw) + Rf0 + 1/hs) - Aex

def df(d, Ds, Q, Tm):
    return (Q / Tm) * (1/(Ds*ht) + Rfi/Ds + (np.log(d/Ds) + 1)/(2*kw))

def newton(dk, Ds, Q, Tm, max_tol):
    iter = 0
    tol = 1
    dk_old = dk

    diffvec = np.array([])
    
    while tol > max_tol and iter < 1000:
        dk = dk_old - f(dk_old, Ds, Q, Tm) / df(dk_old, Ds, Q, Tm)
        tol = np.abs(dk - dk_old)
        dk_old = dk
        diffvec = np.append(diffvec, tol)

        iter += 1
        print("Antal iterationer: ", iter)
        print(tol)

    # Beräkna konvergensordningen för Newtons metod
    konv_ordn = np.zeros(np.size(diffvec))
    kvoter = np.divide(diffvec[1:],diffvec[0:-1])
    konv_ordn = np.divide(np.log(kvoter[1:]),np.log(kvoter[0:-1]))
    konvergens = pd.DataFrame()
    konvergens['Newton konvergensordning'] = konv_ordn
    print(konvergens)

    return dk_old

# Uppgift 2 och 3 a) o b)
print("Uppgift 2:")
d_solution = newton(0.007, Ds, Q, Tm, 10**-8)   # Change to 0.8 for Uppgift 3 c)
print(f"Lösning för d: {d_solution:.6f} m")

# Validate d using root_scalar
result = root_scalar(lambda d: f(d, Ds, Q, Tm), x0=0.007, bracket=[0.001, 0.1], method='brentq')
print(f"Validation with root_scalar: {result.root:.6f} m")
print(f"Difference from Newton's method: {abs(d_solution - result.root):.2e}")

# Uppgift 3 c)
# plot f(d) for d in [0.001, 0.05]
d_values = np.linspace(0, 3, 1000)
f_values = f(d_values, Ds, Q, Tm)
plt.plot(d_values, f_values)
plt.axhline(0, color='red', linestyle='--')
plt.title('Plot of f(d)')
plt.xlabel('d (m)')
plt.ylabel('f(d)')
plt.grid()
plt.show()

# # Uppgift 4
#
# def f1(d, Ds):
#     return Q / (Uf * Tm)