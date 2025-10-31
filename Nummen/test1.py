import numpy as np
import matplotlib.pyplot as plt

# Del a

x = np.array([100.02, 100.04])
y = np.array([ 10.09367, 10.09141])

ones = np.ones(np.shape(x))

Anaiv = np.array([ones, x]).T
print(Anaiv)
c = np.linalg.solve(Anaiv, y)
for i in range(len(c)):
    print(f'c[{i}] = {c[i]}')

print(f"\nThe polynomial is:{c[0]} + {c[1]}x")

pol1 = lambda c, x: c[0] + c[1]*x

pvalue = pol1(c, 100.03)
print(pvalue)

# Plotting

# Create more points for a smooth curve
x_smooth = np.linspace(min(x), max(x), 200)
y_smooth = pol1(c, x_smooth)

plt.plot(x_smooth, y_smooth, 'r-', label='Fitted Polynomial')
plt.plot(x, y, 'bo', label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Newtons method for polynomial fitting
def newton_divided_diff(x, y):
    n = len(y)
    coef = np.copy(y)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef
def newton_poly(coef, x_data, x):
    n = len(coef)
    p = coef[n-1]
    for k in range(n-2, -1, -1):
        p = p * (x - x_data[k]) + coef[k]
    return p
# Given data points
