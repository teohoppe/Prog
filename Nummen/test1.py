# Uppgift 2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

L = 1
x = np.linspace(0, L, 1000)
f = 8/3*x/L - 3*(x/L)**2 + 1/3*(x/L)**3 - 2/3*(np.sin((np.pi*x)/L))

# a)
plt.plot(x, f)
plt.plot([0, L], [0, 0], 'k--')
plt.title("Uppgift 2")
plt.xlabel("x")
plt.ylabel("f(x)")
# plt.show()

# b) Fixpunktsmetoden
def fixed_point_iteration():

    # g(x) ska ge x = g(x) ⇒ nollställe till f(x)
    def fp_fun(x):
        return (3*L/8.0) * (3*(x/L)**2 - (1/3.0)*(x/L)**3 + (2/3.0)*np.sin(np.pi*x/L))

    # startgissning — välj en i intervallet 0 < x < L som konvergerar
    x = 0.2
    tol = 1E-10
    diffv = 5
    i = 0
    diffvec_fp = np.array([])

    while diffv > tol and i < 100:
        i += 1
        xold = x
        x = fp_fun(xold)
        diffv = abs(x - xold)
        diffvec_fp = np.append(diffvec_fp, diffv)
        print(f"Iter {i}: x = {x:.12f}, diff = {diffv:.3e}")

    print(f"\nSlutvärde fixpunkt: x = {x:.12f}")
    print(f"Antal iterationer: {i}")
    print(f"Fel < {tol}\n")

    # Konvergensanalys
    if len(diffvec_fp) > 2:
        S = diffvec_fp[1:] / diffvec_fp[:-1]
        kvoter_fp = np.divide(diffvec_fp[1:], diffvec_fp[:-1])
        konv_ordn = np.divide(np.log(kvoter_fp[1:]), np.log(kvoter_fp[:-1]))
        konvergens = pd.DataFrame({'Fixpunkt konvergensordning': konv_ordn})
        print(konvergens)
    else:
        print("För få iterationer för att bestämma konvergensordning.")

    return x

#fixed_point_iteration()


# c) Newtons metod
def newtons_method():
    
    def f_fun(x):
        return 8/3*x/L - 3*(x/L)**2 + 1/3*(x/L)**3 - 2/3*(np.sin((np.pi*x)/L))
    
    def df_fun(x):
        return 8/3/L - 6*x/L**2 + x**2/L**3 - 2/3*(np.pi/L)*np.cos((np.pi*x)/L)
    
    x = 0.8   # välj startvärde som INTE fungerar för fixpunktmetoden
    tol = 1E-10
    diffv = 1
    iter = 0
    diffvec = np.array([])

    while diffv > tol and iter < 100:
        iter += 1
        f = f_fun(x)
        fp = df_fun(x)
        xnew = x - f / fp
        diffv = abs(xnew - x)
        diffvec = np.append(diffvec, diffv)
        x = xnew
        print(f"Iter {iter}: x = {x:.12f}, diff = {diffv:.3e}")
    
    print(f"\nSlutvärde Newton: x = {x:.12f}")
    print(f"Antal iterationer: {iter}")
    print(f"Fel < {tol}\n")

   
    M = diffvec[1:]/diffvec[0:-1]**2      # Beräkna e_{k+1}/e_k^2 elementvis
    print('')
    print('M = :',M)

    # Beräkna konvergensordningen för Newtons metod
    konv_ordn = np.zeros(np.size(diffvec))
    kvoter = np.divide(diffvec[1:],diffvec[0:-1])  # Beräkna e_{k+1}/e_k elementvis
    konv_ordn = np.divide(np.log(kvoter[1:]),np.log(kvoter[0:-1]))    

    # För tabellutskrift
    konvergens = pd.DataFrame()
    konvergens['Newton konvergensordning'] = konv_ordn

    # Tabell som visar hur metoden konvergerar
    print(konvergens) 

# Kör metoderna
fixed_point_iteration()
newtons_method()
