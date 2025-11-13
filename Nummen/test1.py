import numpy as np
import matplotlib.pyplot as plt

def MK():
    t = np.array([2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
    f_values = np.array([12, 15.10, 19.01, 23.92, 30.11, 37.90, 47.70, 60.03, 75.56])

    # Linjärisering
    x = t - 2016
    y = np.log(f_values)

    # Bygg designmatris
    A = np.vstack([np.ones(len(x)), x]).T

    # Least squares-lösning
    coeffs = np.linalg.solve(A.T @ A, A.T @ y)
    c0, c1 = coeffs
    
    # Omvandla tillbaka
    a = np.exp(c0)
    b = c1

    print(f"a = {a}")
    print(f"b = {b}")

    # Modellfunktion
    def model(t):
        return a * np.exp(b * (t - 2016))

    # Plott
    t_fit = np.linspace(2016, 2024, 500)
    plt.plot(t, f_values, 'o', label="Data")
    plt.plot(t_fit, model(t_fit), label="Minstakvadratanpassning")
    plt.legend()
    plt.show()

MK()
