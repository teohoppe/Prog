import numpy as np
import matplotlib.pyplot as plt

# a)
def q(x):
    return 50*x**3*np.log(x + 1)

def diskretisering_temperatur(q,L, k, TL, TR, N, x_approx= 1.0):
    h = L / N

    xi = np.linspace(h, L-h, num=N-1)

    A = np.zeros((N-1, N-1))
    b = np.zeros(N-1)

    coff = k / (h**2)

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
    A *= coff
    b *= coff
    
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
    plt.plot(x_values, T_values_full, marker='o')
    plt.show()


diskretisering_temperatur(q, 1, 2, 2, 2, 4, 0.2)

diskretisering_temperatur(q, 1, 2, 2, 2, 100, 0.2)

def convergence_study(q, L, k, TL, TR, N):
    exakt_sol = 1.6379544
    error = 1.0
    h_values = []
    approx_sol = 1.0

    while abs(error) > 1e-6:
        h = L / N
        h_values.append(h)
        xi = np.linspace(h, L-h, num=N-1)
        A = np.zeros((N-1, N-1))
        b = np.zeros(N-1)
        coff = k / (h**2)

        for j in range(N-1):
            A[j, j] = -2
            if j > 0:
                A[j, j-1] = 1
            if j < N-2:
                A[j, j+1] = 1

        for j in range(1, N):
            b[j-1] = q(xi[j-1]) * (h**2) / k

        b = b.copy()
        b[0] -= TL
        b[-1] -= TR
        A *= coff
        b *= coff
        T_values = np.linalg.solve(A, b)
        x_values = np.linspace(0, L, N+1)
        T_values_full = np.zeros(N+1)
        T_values_full[0] = TL
        T_values_full[-1] = TR
        T_values_full[1:-1] = T_values
        approx_sol = np.interp(0.7, x_values, T_values_full)
        error = abs(exakt_sol - approx_sol)
        N *= 2
        
    print(f"Slutligt N: {N//2}, Approximerad temperatur vid x=0.7: {approx_sol:.7f}, Fel: {error:.7e}")

convergence_study(q, 1, 2, 2, 2, 50)