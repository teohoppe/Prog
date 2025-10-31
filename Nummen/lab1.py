import numpy as np
import matplotlib.pyplot as plt
# Del a

def naiv_ansats():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    y = np.array([421, 553, 709, 871, 1021, 1109, 1066, 929, 771, 612, 463, 374])

    Anaiv = np.vander(x,12, increasing=True)
    #print(Anaiv)

    c = np.linalg.solve(Anaiv, y)
    # for i in range(len(c)):
    #     print(f'c[{i}] = {c[i]}')

    #print(f"\nThe polynomial is:{c[0]} + {c[1]}x + {c[2]}x^2 + {c[3]}x^3 + {c[4]}x^4 + {c[5]}x^5 + {c[6]}x^6 + {c[7]}x^7 + {c[8]}x^8 + {c[9]}x^9 + {c[10]}x^10 + {c[11]}x^11")

    pol1 = lambda c, x: c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3 + c[4]*x**4 + c[5]*x**5 + c[6]*x**6 + c[7]*x**7 + c[8]*x**8 + c[9]*x**9 + c[10]*x**10 + c[11]*x**11

    pvalue = pol1(c, 6.5)
    print(pvalue)

    # Plotting

    # Create more points for a smooth curve
    x_smooth = np.linspace(x[0], x[-1], 1000)
    y_smooth = pol1(c, x_smooth)

    plt.plot(x_smooth, y_smooth, 'r-', label='Fitted Polynomial')
    plt.plot(x, y, 'bo', label='Data Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

naiv_ansats()

# Newtons method for polynomial fitting
def newton_ansats():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    y = np.array([421, 553, 709, 871, 1021, 1109, 1006, 929, 771, 612, 463, 374])




    ones = np.ones(np.shape(x))
