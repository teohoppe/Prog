import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# a ) - c)

# Circuit parameters
R = 1
C = 0.5
L = 2

# Initial conditions and time span
U0 = [0, 1]
t_span = [0, 2]
q = np.array(U0)

# Initial conditions and time span
U0 = [1, 0]
t_span = [0, 20]
q = np.array(U0)

# ODE function
def ODE_function(t, q, R, C, L):
    dqdt = np.zeros(2)
    dqdt[0] = q[1]
    dqdt[1] = -R*q[1]/L - q[0]/(L*C)
    return dqdt

# Inbydgd referenslösning med hög noggrannhet
solution = solve_ivp(ODE_function, t_span, U0, args= (R, C, L), t_eval= np.linspace(t_span[0], t_span[-1], 1000), rtol=1e-8,atol=1e-10)
print("Referenslösning vid T=2:", solution.y[:, -1])

# d)
def stable(ODE_function, N, R, C, L):
    # Gör fulla euler framåt implementation
    def euler_forward_full(ODE_function, y0, t0, tspan, N, R, C, L):
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
    
    stable = []

    for n in N:
        t_euler, y_euler = euler_forward_full(ODE_function, U0, t_span[0], t_span, n, R, C, L)

        if np.max(np.abs(y_euler)) < 5 * np.max(np.abs(solution.y)):
            stable.append(n)

        # Plottar resultatet
        plt.plot(t_euler, y_euler[:, 0], label=f'Euler N={n}')
        plt.plot(solution.t, solution.y[0], 'k-', label='Referenslösning')
        plt.xlabel('Tid (s)')
        plt.ylabel('Spänning (V)')
        plt.title('Spänning över tid i RLC-krets')
        plt.xlim(left=0)
        plt.grid()
        plt.legend()
        plt.show()

    print('Stabila N-värden för Euler framåt:', stable)
    return stable

def euler_forward(f, y0, t0, t1, N, R, C, L):
    h = (t1 - t0) / N
    h = 0.02
    t = t0
    y = y0

    for n in range(N):
        y = y + h * f(t, y, R, C, L)
        t += h

    return y

# e)

def if_stable():

    # --- Referenslösning ---
    sol_ref = solve_ivp(ODE_function, t_span, U0, args=(R, C, L), t_eval=[t_span[-1]], rtol=1e-12, atol=1e-14)

    y_ref = sol_ref.y[:, -1]   # [q(T), i(T)]

    print("Referenslösning y1 =", y_ref[0])
    print("\nReferenslösning y2 =", y_ref[1])

    # --- Lista på N som antas stabila ---
    stable_N = [40, 80, 160, 320, 640, 1280, 2560, 5120, 10240]

    errors = []
    errors1 = []
    h_values = []
    uN_values = []
    uN1_values = []

    for n in stable_N:
        h = (t_span[-1] - t_span[0]) / n
        h_values.append(h)

        # Euler framåt
        yN = euler_forward(ODE_function, U0, t_span[0], t_span[-1], n, R, C, L)

        uN1 = yN[0]  
        uN = yN[1] 
        uN1_values.append(uN1)
        uN_values.append(uN)

        # Beräkna fel för båda komponenterna
        error = abs(y_ref[1] - uN)
        errors.append(error)
        error1 = abs(y_ref[0] - uN1)
        errors1.append(error1)

        print(f"h = {h:.6f},   y1 = {uN1:.10f},  Fel y1 = {error1:.3e}")
        print(f"h = {h:.6f},   y2 = {uN:.10f},   Fel y2= {error:.3e}")

    # --- Noggrannhetsordning ---
    print("\nNoggrannhetsordning p1:")
    for i in range(len(errors1)-1):
        p1 = np.log2(errors1[i] / errors1[i+1])
        print(f"N={stable_N[i]:5d} → N={stable_N[i+1]:5d},   p1 = {p1:.6f}")

    print("\nNoggrannhetsordning p2:")
    for i in range(len(errors)-1):
        p = np.log2(errors[i] / errors[i+1])
        print(f"N={stable_N[i]:5d} → N={stable_N[i+1]:5d},   p = {p:.6f}")


if_stable()

plt.plot(solution.t, solution.y[0], 'b-')
plt.xlabel('Tid (s)')
plt.ylabel('Spänning (V)')
plt.title('Spänning över tid i RLC-krets')
plt.xlim(left=0)
plt.grid()
plt.show()

# Euler framåt (Explicit Euler):
# y_{n+1} = y_n + h * f(t_n, y_n)

# Euler bakåt (Implicit Euler):
# y_{n+1} = y_n + h * f(t_{n+1}, y_{n+1})

# Nogranhetsordning för både Euler framåt och Euler bakåt är p = 1, vilket innebär att felet minskar linjärt med steglängden h.