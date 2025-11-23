import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from lab2_F import convergence_study

# a ) - c)

# Circuit parameters
R = 1
C = 0.5
L = 2

# Initial conditions and time span
U0 = [1, 0]
t_span = [0, 20]
q = np.array(U0)

def ODE_function(t, q, R, C, L):
    dqdt = np.zeros(2)
    dqdt[0] = q[1]
    dqdt[1] = -R*q[1]/L - q[0]/(L*C)
    return dqdt

# Solve the ODE
solution = solve_ivp(ODE_function, t_span, U0, args= (R, C, L), t_eval= np.linspace(t_span[0], t_span[-1], 100), rtol=1e-8,atol=1e-10)

# d)
def euler_forward1(ODE_function, y0, t0, tspan, N, R, C, L):
    def euler_forward(ODE_function, y0, t0, tspan, N, R, C, L):
        h = (tspan[-1] - t0) / N
        t = t0
        
        tvec =np.linspace(t0, tspan[-1], N+1)
        yy = np.array(U0)
        Y = [yy]

        for n in range(N):
            tt = tvec[n]  # lokal tid
            ff = ODE_function(tt, yy, R, C, L)  # Evaluera funktionen
            yy = yy + h * ff  # Updatera lösningen med Euler framåt
            Y.append(yy)  # Lagra lösningen i en matris

        Y = np.array(Y)
        return tvec, Y

    N = [20, 40, 80, 160]
    stable = []

    for n in N:
        t_euler, y_euler = euler_forward(ODE_function, U0, t_span[0], t_span, n, R, C, L)

        if np.max(np.abs(y_euler)) < 5 * np.max(np.abs(solution.y)):
            stable.append(n)

        plt.plot(t_euler, y_euler[:, 0], label=f'Euler N={n}')
        plt.plot(solution.t, solution.y[0], 'k-', label='Referenslösning')
        plt.xlabel('Tid (s)')
        plt.ylabel('Spänning (V)')
        plt.title('Spänning över tid i RLC-krets')
        plt.xlim(left=0)
        plt.grid()
        plt.legend()
        #plt.show()

    print('Stabila N-värden för Euler framåt:', stable)
    return stable

stable_N = euler_forward1(ODE_function, U0, t_span[0], t_span, N=160, R=R, C=C, L=L)

# fel ish
def con_study(euler_forward, f, T, exact_solution):
    h_values = []
    for n in stable_N:
        h = (t_span[-1] - t_span[0]) / n
        h_values.append(h)

    uN_values = []  # lista för att lagra y(T) för varje h

    for h in h_values:
        uN = euler_forward(f, 1, 0, T, h, )[1][-1]
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

con_study(euler_forward1, ODE_function, t_span[-1], lambda t: np.interp(t, solution.t, solution.y[0]))



print('Lösningen blir ',solution.y[0])
plt.plot(solution.t, solution.y[0], 'b-')
plt.xlabel('Tid (s)')
plt.ylabel('Spänning (V)')
plt.title('Spänning över tid i RLC-krets')
plt.xlim(left=0)
plt.grid()
plt.show()