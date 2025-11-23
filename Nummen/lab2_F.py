import numpy as np
import matplotlib.pyplot as plt

T = 1.2

def f(t, y):
    return 1 + t - y

def euler_forward(f, y0, t0, T, h):
    n = round((T - t0) / h)
    t_values = np.linspace(t0, T, n+1)
    y_values = np.zeros(n+1)

    y = y0
    y_values[0] = y0
    tvec = [t0]
    yvec = [y0]

    for i in range(n):
        y = y + h * f(t_values[i], y)
        y_values[i+1] = y
        tvec.append(t_values[i+1])
        yvec.append(y)
        print(f"t = {t_values[i+1]:.1f}, y = {y:.6f}")

    return tvec, yvec

t, y = euler_forward(f, 1, 0, T, 0.1)

def exact_solution(t):
    return np.exp(-t) + t

print("Exakt lösning vid T=1.2:", exact_solution(T))


# F2 a) and b) and c)
def convergence_study(t, euler_forward, f, T, exact_solution):
    h_values = [0.2, 0.1, 0.05, 0.025, 0.0125]

    uN_values = []  # lista för att lagra y(T) för varje h

    for h in h_values:
        uN = euler_forward(f, 1, 0, T, h)[1][-1]
        uN_values.append(uN)
        print(f"h = {h:.4f}  y = {uN:.6f}\n")
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

plt.plot(t, y, 'b*:')
plt.clf()
plt.plot(t, y, 'r-')
plt.scatter(t, y, c='blue', marker='o')
plt.grid()
plt.title("Euler framåt för y' = 1 + t - y")
plt.xlabel("t")
plt.ylabel("y")
plt.show()