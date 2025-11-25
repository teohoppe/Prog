import numpy as np

# data
L = 1.0
k = 2.0
TL = 2.0
TR = 2.0
N = 4
h = L / N

def q(x):
    return 50 * x**3 * np.log(x + 1)

# inre punkter x1..x_{N-1}
x = np.array([h*j for j in range(1, N)])   # [0.25, 0.5, 0.75]

# rå högerled (utan randvillkor)
b_raw = (h**2 / k) * np.array([q(xi) for xi in x])

# ta in randvillkoren
b = b_raw.copy()
b[0] -= TL
b[-1] -= TR

# om du vill visa "din" matris A_raw och b (icke-skalad)
A_raw = np.array([[-2, 1, 0],
                  [ 1,-2, 1],
                  [ 0, 1,-2]])

print("A_raw:")
print(A_raw)
print("\nb (efter att ha subtraherat randvillkor) = b_raw with TL/TR adjustments:")
print(b)

# Uppgiftens format: A_up = (k/h^2) * A_raw, HL = (k/h^2) * b
scale = k / h**2
A_up = scale * A_raw
HL = scale * b

print("\nSkalningsfaktor (k/h^2) =", scale)
print("\nA (i uppgiftens form):")
print(A_up)
print("\nHL (i uppgiftens form):")
print(HL)
