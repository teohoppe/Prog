import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags

# a)
def q(x):
    return 50*x**3*np.log(x + 1)

def diskretisering_temperatur(q,L, k, TL, TR, N, x_approx= 1.0):
    h = L / N

    xi = np.linspace(h, L-h, num=N-1)

    A = np.zeros((N-1, N-1))
    b = np.zeros(N-1)

    coeff = k / (h**2)

    for j in range(N-1):
        A[j, j] = -2
        if j > 0:
            A[j, j-1] = 1
        if j < N-2:
            A[j, j+1] = 1

    for j in range(1, N):  # x_1 ... x_{N-1}
        b[j-1] = q(xi[j-1]) * (h**2) / k
    
    b = b.copy()
    b[0] -= TL
    b[-1] -= TR
    A *= coeff
    b *= coeff

    print("Matris A:")
    print(A)
    print("\nHögerled b:")
    print(b)
    
    T_values = np.linalg.solve(A, b)
    x_values = np.linspace(0, L, N+1)
    T_values_full = np.zeros(N+1)
    T_values_full[0] = TL
    T_values_full[-1] = TR
    T_values_full[1:-1] = T_values
    T_approx = np.interp(x_approx, x_values, T_values_full)
    print(f"\nApproximerad temperatur vid x={x_approx}: {T_approx:.4f} °C")
    
    plt.title(f"Diskretisering med N={N} punkter")
    plt.xlabel("Position längs stången (m)")
    plt.ylabel("Temperatur (°C)")
    plt.grid()
    plt.plot(x_values, T_values_full, "b-")
    plt.show()
    
    return T_approx

# c)
#diskretisering_temperatur(q, 1, 2, 2, 2, 4, 0.2)

# d)
diskretisering_temperatur(q, 1, 2, 4, 2, 100, 0.2)

# e)
def convergence_study(q, L, k, TL, TR, N):
    exakt_sol = 1.6379544
    error = 1.0
    error_list = []
    N_list = [] 

    while abs(error) > 1e-6:
        T_approx = diskretisering_temperatur(q, L, k, TL, TR, N, x_approx=0.7)
        error = exakt_sol - T_approx
        error_list.append(error)
        N_list.append(N)    
        print(f"N={N}, Approximerad temperatur vid x=0.7: {T_approx:.7f}, Fel: {error:.7e}\n")
        N *= 2
        # Nogranhetsordning p

    if len(error_list) >= 3:
        p = np.log2(abs(error_list[0] - error_list[1]) / abs(error_list[1] - (error_list[2])))
        print(f"P går mot {p} ")

#convergence_study(q, 1, 2, 2, 2, 50)