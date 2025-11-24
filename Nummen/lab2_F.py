import numpy as np
import matplotlib.pyplot as plt

T = 1.2

# Vår differentialekvation
def f(t, y):
    return 1 + t - y

# a) Euler framåt implementation
def euler_forward(f, y0, t0, T, h):
    n = round((T - t0) / h)                 # antal steg
    t_values = np.linspace(t0, T, n+1)      # tidspunkter
    y_values = np.zeros(n+1)           # array för y-värden

    y = y0              # strartvärde
    y_values[0] = y0    # sätt första värdet
    tvec = [t0]         # lista för tidpunkter och sätter in vårt startvärde 
    yvec = [y0]         # lista för y-värden och sätter in vårt startvärde 

    # Iterera över varje steg och beräkna y-värdet med Euler framåt
    for i in range(n):
        y = y + h * f(t_values[i], y)   # Euler framåt formel
        y_values[i+1] = y               # spara y-värdet
        tvec.append(t_values[i+1])      # spara tidpunkten
        yvec.append(y)              # spara y-värdet
        print(f"t = {t_values[i+1]:.1f}, y = {y:.6f}")  # skriv ut t och y-värdet

    return tvec, yvec   # returnera tidpunkter och y-värden

# tar ut t och y värde från euler_forward
t, y = euler_forward(f, 1, 0, T, 0.1)

# exakt lösning
def exact_solution(t):
    return np.exp(-t) + t

print("Exakt lösning vid T=1.2:", exact_solution(T))


# F2 a) and b) and c)
def convergence_study(t, euler_forward, f, T, exact_solution):
    h_values = [0.2, 0.1, 0.05, 0.025, 0.0125]  # alla olika h värden 

    uN_values = []  # lista för att lagra y(T) för varje h

    # loopar igenom alla h värden och beräknar y(T) med euler_forward
    for h in h_values:
        uN = euler_forward(f, 1, 0, T, h)[1][-1]    # tar ut sista y värdet från euler_forward
        uN_values.append(uN)                         # lägger till y(T) i listan
        print(f"h = {h:.4f}  y = {uN:.6f}\n")       # skriver ut h och y(T)
        # beräknar och skriver ut felet
        error = abs(exact_solution(T) - uN)
        print(f"Fel vid h = {h:.4f}: {error:.6e}\n")

    print("Slutvärden uN för olika h:")
    for i in range(len(h_values)):
        print(f"h = {h_values[i]:.4f}  y = {uN_values[i]:.6f}")
        print(f"Fel vid h = {h_values[i]:.4f}: {abs(exact_solution(T) - uN_values[i]):.6e}")

    for i in range(len(h_values)-1):
        p = np.log2((np.abs(exact_solution(T) - uN_values[i]) / np.abs(exact_solution(T) - uN_values[i+1]))).round(3)
        print(f"Nogranhetsordningen p = {p}")

convergence_study(t, euler_forward, f, T, exact_solution)

# plotta allt
plt.plot(t, y, 'b*:')
plt.clf()
plt.plot(t, y, 'r-')
plt.scatter(t, y, c='blue', marker='o')
plt.grid()
plt.title("Euler framåt för y' = 1 + t - y")
plt.xlabel("t")
plt.ylabel("y")
plt.show()