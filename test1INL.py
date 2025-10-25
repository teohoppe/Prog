# Data från tabellen (p4 = 6, p6 = 5)
eta = 13
L = 4.9
Ns = 40
m = 11

# Balkens dimensioner
t = 20e-3          # tjocklek [m]
B = eta * t        # bredd [m]
H = eta * t        # höjd [m]

# Tröghetsmoment (rektangel-approximation)
I = (B * H**3) / 12
y = H / 2

# Massor
mlok = 77e3        # [kg]
mvagn = 54e3       # [kg]
g = 9.82           # [m/s^2]

# Krafter
Plok = mlok * g
Pvagn = mvagn * g

# Böjmoment (last mitt på balk)
Mlok = Plok * L / 4
Mvagn = Pvagn * L / 4

# Spänningar i fläns
sig_lok = Mlok * y / I / 1e6   # [MPa]
sig_vagn = Mvagn * y / I / 1e6 # [MPa]

print(f"sig_lok = {sig_lok:.2f} MPa")
print(f"sig_vagn = {sig_vagn:.2f} MPa")
