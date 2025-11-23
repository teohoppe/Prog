import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ============================
#   PARAMETRAR
# ============================
L = 2
C = 0.5
R = 1

# ODE-systemet
def F(t, y):
    q, i = y
    dqdt = i
    didt = -(R/L) * i - (1/(L*C)) * q
    return [dqdt, didt]


# ============================
#   EULER FRAMÅT
# ============================
def euler_forward_system(F, y0, t0, T, N):
    h = (T - t0) / N
    t = t0
    y = np.array(y0, float)

    t_list = [t]
    y_list = [y.copy()]

    for _ in range(N):
        y = y + h * np.array(F(t, y))
        t = t + h
        t_list.append(t)
        y_list.append(y.copy())

    return np.array(t_list), np.array(y_list)


# ============================
#   REFERENSLÖSNING
# ============================
y0 = [1, 0]
t_span = (0, 20)

sol = solve_ivp(F, t_span, y0, method="RK45", rtol=1e-8, atol=1e-10, dense_output=True)
t_ref = np.linspace(0, 20, 2000)
y_ref = sol.sol(t_ref)


# ============================
#   N-VÄRDEN
# ============================
N_values = [20, 40, 80, 160]

stable = []
unstable = []


# ============================
#   LOOP FÖR ALLA N
# ============================
for N in N_values:

    t_e, y_e = euler_forward_system(F, y0, 0, 20, N)

    # Plotta q(t)
    plt.figure(figsize=(8,4))
    plt.plot(t_ref, y_ref[0], label="Referens q(t)")
    plt.plot(t_e, y_e[:,0], "o--", label=f"Euler q(t), N={N}")
    plt.grid()
    plt.xlabel("t")
    plt.ylabel("q(t)")
    plt.title(f"q(t) jämförelse – N={N}")
    plt.legend()
    plt.show()

    # Plotta i(t)
    plt.figure(figsize=(8,4))
    plt.plot(t_ref, y_ref[1], label="Referens i(t)")
    plt.plot(t_e, y_e[:,1], "o--", label=f"Euler i(t), N={N}")
    plt.grid()
    plt.xlabel("t")
    plt.ylabel("i(t)")
    plt.title(f"i(t) jämförelse – N={N}")
    plt.legend()
    plt.show()

    # Enkel stabilitetskoll: om Euler blåser upp jämfört med referens
    if np.max(np.abs(y_e)) > 5 * np.max(np.abs(y_ref)):
        unstable.append(N)
    else:
        stable.append(N)


# ============================
#   RESULTAT
# ============================
print("\nRESULTAT:")
print("Stabila N:", stable)
print("Instabila N:", unstable)
