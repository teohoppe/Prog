import numpy as np
# Uppgift 2 och 3 i Hålf B

#För dubbell kantspricka (uppgift 2)
# Parametrar
KIc = 50
KI0 = 1
C = 4.2e-12
n = 3.5
L = 4.9
eta = 13
m = 11          # Antal vagnar
Ns = 40         # Antal tåg per dag
t = 20e-3       # Tjocklek [m]
B = eta * t     # Bredd [m]
H = eta * t     # Höjd [m]
sig_lok = 65.9  # Uträknade värden från upp1
sig_vagn = 60.9 # Uträknade värden från upp1


# Startvärden
a0 = t
W = B
Ntag = 20000


# Koefficienter för f(a/W)
alpha = [1.1215, -0.5699, -0.7056,
2.4748, -3.1194, 1.8945, -0.4594]


# För att hålla koll på spricklängd över tid
aN = a0 * np.ones(Ntag)


# Definiera F4 som en funktion för a/W
def F4(a, W):
    sum_faw = 0
    for i in range(len(alpha)):
        sum_faw += alpha[i] * ((a/W)**i)
    return sum_faw / np.sqrt(1 -(a/W))

def F5(a, W):
    return ((((2 * W) / (np.pi* a)) * np.tan((np.pi* a) / (2* W))) **(1/2))* (np.cos((np.pi *a) / (2 *W))) ** (-1) * (0.752+ (2.02 * (a / W)) +(0.37 * (1 - np.sin((np.pi* a) / (2* W))) ** 3))


# Startvärde på spricklängden
a = a0

def upp2(a, W):
    # Loopen för att uppdatera spricklängden
    for k in range(Ntag):
        f4 = F4(a, W)  # Beräkna f4 för nuvarande a och W
        KI = sig_lok * np.sqrt(np.pi* a) * f4  # Beräkna KI
        da = 2 * C * ((KI / KI0) **n)
        a = a + da  # Uppdatera spricklängden


        for j in range(m):
            f4 = F4(a, W)
            KI = sig_vagn * np.sqrt(np.pi* a) * f4  # Beräkna KI
            da = 2 * C * ((KI / KI0) **n)
            a = a + da  # Uppdatera spricklängden
        aN[k] = a  # Spara spricklängden


        # Beräkna KI för sista värdet
        KI = sig_lok * np.sqrt(np.pi* a) * F4(a, W)


        # Kolla om sprickan når kritisk längd
        if KI > KIc:
            print(f"Efter {k+1} tåg är sprickan av kritisk längd, a = {a:.4f} meter")
            print(f"Vilket är {(k+1)/Ns}dagar")
            break  # Avbryter om sprickan nått kritisk längd

    else:
        print(f"Sprickan nådde aldrig kritisk längd. Slutlängd: a = {a:.4f}meter")


def upp3(a, W):
    # Loopen för att uppdatera spricklängden
    for k in range(Ntag):
        f5 = F5(a, W)  # Beräkna f4 för nuvarande a och W
        KI = sig_lok * np.sqrt(np.pi* a) * f5  # Beräkna KI
        da = 2* C * ((KI / KI0) **n)
        a = a + da  # Uppdatera spricklängden


        for j in range(m):
            f5 = F5(a, W)
            KI = sig_vagn * np.sqrt(np.pi* a) * f5  # Beräkna KI
            da = 2 * C * ((KI / KI0) **n)
            a = a + da  # Uppdatera spricklängden
        aN[k] = a  # Spara spricklängden


        # Beräkna KI för sista värdet
        KI = sig_lok * np.sqrt(np.pi* a) * F5(a, W)


        # Kolla om sprickan når kritisk längd
        if KI > KIc:
            print(f"Efter {k+1} tåg är sprickan av kritisk längd, a = {a:.4f} meter")
            print(f"Vilket är {(k+1)/Ns}dagar")
            break  # Avbryter om sprickan nått kritisk längd


    else:
        print(f"Sprickan nådde aldrig kritisk längd. Slutlängd: a = {a:.4f}meter")

if __name__ == "__main__":
    while True:
        choise = input("Uppgift 2 eller 3?  ")
        if choise == "2":
            a = a0
            upp2(a, W)
        elif choise == "3":
            a = a0
            upp3(a, W)
        else:
            break
    
        