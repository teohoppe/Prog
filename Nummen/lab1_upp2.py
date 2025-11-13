# Uppgift 2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# a)

def plot_function():
    L = 1
    x = np.linspace(0, L, 1000)
    y = 0
    f = 8/3*x/L - 3*(x/L)**2 + 1/3*(x/L)**3 - 2/3*(np.sin((np.pi*x)/L))

    plt.plot(x, f,)
    plt.plot([0, L], [0, 0], 'k--')
    plt.title("Upp2")
    plt.xlabel("L")
    plt.ylabel("Y") 
    plt.show()

# b)
def find_zero_points():
    L = 1
    zero_points = [0, 0.3, 0.8, 1]

    def g(x):
        g1 = 3/8*L*(3*(x/L)**2 -1/3*(x/L)**3 + 2/3*np.sin((np.pi*x)/L))
        return g1
    
    def gprim(x):
        gprim1 = 3/8*L*(6*x/L**2 - x**2/L**3 + 2/3*(np.pi/L)*np.cos((np.pi*x)/L))
        return gprim1
    
    print(g(0.3))
    print(gprim(0.3))

    for i in range(len(zero_points)):
        print(f"g({zero_points[i]}) = {g(zero_points[i])}")
        print(f"g'({zero_points[i]}) = {gprim(zero_points[i])}")
        if abs(gprim(zero_points[i])) < 1:
            print(f"Fixpunktssatsen är uppfylld vid x = {zero_points[i]}")


# c)
def fixed_point_iteration():
    print("Fixpunktsmetoden")
    L = 1
    x = np.linspace(0, L, 1000)
    
    def fp_fun(x):
        g = (3*L/8.0) * (3*(x/L)**2 - (1/3.0)*(x/L)**3 + (2/3.0)*np.sin(np.pi*x/L))
        return g

    # Initialise variables
    x = 0.85
    tol = 1E-10
    diffv = 5
    i = 0
    diffvec_fp = []

    while diffv > tol and i < 1000:
        i += 1
        xold = x
        x = fp_fun(xold)
        diffv = abs(x-xold)
        diffvec_fp = np.append(diffvec_fp,diffv)  
        print('')
        print(i, x, diffv)

    # Calculate and print convergence order
    S = diffvec_fp[1:]/diffvec_fp[0:-1]      
    print('')
    print('S = :',S)    

    konv_ordn = np.zeros(np.size(diffvec_fp))
    kvoter_fp = np.divide(diffvec_fp[1:],diffvec_fp[0:-1]) 
    konv_ordn = np.divide(np.log(kvoter_fp[1:]),np.log(kvoter_fp[0:-1]))    

    konvergens = pd.DataFrame()
    konvergens['Fixpunkt konvergensordning'] = konv_ordn

    print(konvergens)  
    return diffvec_fp


# d)
def newtons_method():
    print("Newtons metod")
    L = 1

    def f_fun():
        f = 8/3*x/L - 3*(x/L)**2 + 1/3*(x/L)**3 - 2/3*(np.sin((np.pi*x)/L))
        return f
    
    def df_fun():
        df = 8/3/L - 6*x/L**2 + x**2/L**3 - 2/3*(np.pi/L)*np.cos((np.pi*x)/L)
        return df
    
    x = 0.3
    # Given tolerens
    tol = 1E-10
    # Initiera slingan
    diffv = 1
    # Räkna iterationer
    iter = 0
    # Initiera en tom lista
    diffvec = np.array([])

    # Iterera fram en lösning
    while diffv > tol and iter < 1000:
        iter += 1
        f,fp = f_fun(),df_fun()
        xnew = x-f/fp
        diffv = abs(xnew-x)
        diffvec = np.append(diffvec,diffv)   # Lägg diffv sist i listan diffvec
        x = xnew
        print('')
        print(iter, x, diffv)
        
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
    return diffvec

# e) 

def compare_convergence():
    print("\nJämförelse av konvergenshastighet\n")
    
    L = 1
    x0 = 0.8  # Common starting point
    tol = 1e-10
    max_iter = 1000

    def g(x):
        return (3*L/8.0)*(3*(x/L)**2 - (1/3)*(x/L)**3 + (2/3)*np.sin(np.pi*x/L))

    def f(x):
        return 8/3*x/L - 3*(x/L)**2 + 1/3*(x/L)**3 - 2/3*np.sin(np.pi*x/L)

    def df(x):
        return 8/3/L - 6*x/L**2 + x**2/L**3 - 2/3*(np.pi/L)*np.cos(np.pi*x/L)

    # Fixedpoint 
    x = x0
    fp_errors = []
    for _ in range(max_iter):
        x_new = g(x)
        fp_errors.append(abs(x_new - x))
        if abs(x_new - x) < tol:
            break
        x = x_new

    # Newtons
    x = x0
    newton_errors = []
    for _ in range(max_iter):
        x_new = x - f(x)/df(x)
        newton_errors.append(abs(x_new - x))
        if abs(x_new - x) < tol:
            break
        x = x_new

    plt.semilogy(fp_errors, label="Fixpunkt")
    plt.semilogy(newton_errors, label="Newton")
    plt.xlabel("Iteration n")
    plt.ylabel("|xₙ₊₁ − xₙ|")
    plt.title("Konvergensjämförelse")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Fixpunkt sista fel:", fp_errors[-1])
    print("Newton sista fel:", newton_errors[-1])


def main_menu():
    while True:
        print("\nVälj en funktion att köra:")
        print("1. Plotta funktion (a)")
        print("2. Nollställen och fixpunktssats (b)")
        print("3. Fixpunktsmetoden (c)")
        print("4. Newtons metod (d)")
        print("5. Jämför konvergenshastighet (e)")
        print("6. Avsluta")

        choice = input("Ange val (1-5): ")

        if choice == "1":
            plot_function()
        elif choice == "2":
            find_zero_points()
        elif choice == "3":
            fixed_point_iteration()
        elif choice == "4":
            newtons_method()
        elif choice == "5":
            compare_convergence()
        elif choice == "6":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main_menu()