import numpy as np
import matplotlib.pyplot as plt
# Del a)

def naiv_ansats():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    y = np.array([421, 553, 709, 871, 1021, 1109, 1066, 929, 771, 612, 463, 374])

    Anaiv = np.vander(x,12, increasing=True)
    print(Anaiv)

    c = np.linalg.solve(Anaiv, y)
    for i in range(len(c)):
        print(f'c[{i}] = {c[i]}')

    print(f"\nThe polynomial is:{c[0]} + {c[1]}x + {c[2]}x^2 + {c[3]}x^3 + {c[4]}x^4 + {c[5]}x^5 + {c[6]}x^6 + {c[7]}x^7 + {c[8]}x^8 + {c[9]}x^9 + {c[10]}x^10 + {c[11]}x^11")

    pol1 = lambda c, x: c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3 + c[4]*x**4 + c[5]*x**5 + c[6]*x**6 + c[7]*x**7 + c[8]*x**8 + c[9]*x**9 + c[10]*x**10 + c[11]*x**11

    pvalue = pol1(c, 6.5)
    print(pvalue)

    # Plotting
    x_smooth = np.linspace(x[0], x[-1], 1000)
    y_smooth = pol1(c, x_smooth)

    plt.plot(x_smooth, y_smooth, 'r-', label='Fitted Polynomial')
    plt.plot(x, y, 'bo', label='Data Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def newton_ansats():
    xdata = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    ydata = np.array([421, 553, 709, 871, 1021, 1109, 1066, 929, 771, 612, 463, 374])

    p1 = lambda xx,xd: xx - xd[0]
    p2 = lambda xx,xd: (xx -xd[0])*(xx -xd[1])
    p3 = lambda xx,xd: (xx - xd[0])*(xx -xd[1])*(xx -xd[2])
    p4 = lambda xx,xd: (xx - xd[0])*(xx -xd[1])*(xx - xd[2])*(xx -xd[3]) 
    p5 = lambda xx,xd: (xx - xd[0])*(xx -xd[1])*(xx - xd[2])*(xx -xd[3])*(xx -xd[4])
    p6 = lambda xx,xd: (xx - xd[0])*(xx -xd[1])*(xx - xd[2])*(xx -xd[3])*(xx -xd[4])*(xx -xd[5])
    p7 = lambda xx,xd: (xx - xd[0])*(xx -xd[1])*(xx - xd[2])*(xx -xd[3])*(xx -xd[4])*(xx -xd[5])*(xx -xd[6])
    p8 = lambda xx,xd: (xx - xd[0])*(xx -xd[1])*(xx - xd[2])*(xx -xd[3])*(xx -xd[4])*(xx -xd[5])*(xx -xd[6])*(xx -xd[7])
    p9 = lambda xx,xd: (xx - xd[0])*(xx -xd[1])*(xx - xd[2])*(xx -xd[3])*(xx -xd[4])*(xx -xd[5])*(xx -xd[6])*(xx -xd[7])*(xx -xd[8])
    p10 = lambda xx,xd: (xx - xd[0])*(xx -xd[1])*(xx - xd[2])*(xx -xd[3])*(xx -xd[4])*(xx -xd[5])*(xx -xd[6])*(xx -xd[7])*(xx -xd[8])*(xx -xd[9])
    p11 = lambda xx,xd: (xx - xd[0])*(xx -xd[1])*(xx - xd[2])*(xx -xd[3])*(xx -xd[4])*(xx -xd[5])*(xx -xd[6])*(xx -xd[7])*(xx -xd[8])*(xx -xd[9])*(xx -xd[10])

    ones = np.ones(np.shape(xdata))
    Anewt = np.array([ones,p1(xdata,xdata),p2(xdata,xdata),p3(xdata,xdata),p4(xdata,xdata),p5(xdata,xdata),p6(xdata,xdata),p7(xdata,xdata),p8(xdata,xdata),p9(xdata,xdata),p10(xdata,xdata),p11(xdata,xdata)]).T 
    print(Anewt)
    
    a = np.linalg.solve(Anewt, ydata)
    for i in range(len(a)):
        print(f'a[{i}] = {a[i]}')

    def polyNewton(a,xd,x):
        prodpoly = np.ones((len(x)))      
        sumpoly = a[0]*np.ones((len(x)))  
        for n in range(1,len(a)):         
            prodpoly = np.multiply(prodpoly,x-xd[n-1])   
            sumpoly += a[n]*prodpoly  
        return sumpoly
    
    xfine = np.linspace(xdata[0], xdata[-1],1000)
    yfine = polyNewton(a,xdata,xfine)

    # Plotta datapunkter och polynom
    plt.plot(xdata,ydata,'bo')
    plt.plot(xfine,yfine,'r-', label='Fitted Polynomial')
    plt.title('Interpolation polynomial and data, Newtons ansatz')
    plt.plot(xdata, ydata, 'bo', label='Data Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def centrerad_ansats():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    y = np.array([421, 553, 709, 871, 1021, 1109, 1066, 929, 771, 612, 463, 374])

    x_mean = np.mean(x)
    x_mean_centerd = x - x_mean
    Acenterd = np.vander(x_mean_centerd, 12, increasing=True)
    print(Acenterd)

    c = np.linalg.solve(Acenterd, y)
    for i in range(len(c)):
        print(f'c[{i}] = {c[i]}')

    def pol_centrerad(c, x, x_mean):
        return sum(c[i] * (x - x_mean)**i for i in range(len(c)))

    # Rita ut
    x_smooth = np.linspace(x[0], x[-1], 1000)
    y_smooth = pol_centrerad(c, x_smooth, x_mean)

    plt.plot(x, y, 'bo', label='Datapunkter')
    plt.plot(x_smooth, y_smooth, 'r-', label='Centrerad ansats')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Polynominterpolation - Centrerad ansats')
    plt.legend()
    plt.grid(True)
    plt.show()
        

# Del c)

def MK_ansats():
    x = np.array([4, 5, 6, 7, 8])
    y = np.array([871, 1021, 1109, 1066, 929])

    ones = np.ones(np.shape(x))
    A = np.array([ones, x, x**2]).T
    print(A)

    aTa = A.T @ A
    aTy = A.T @ y

    c = np.linalg.solve(aTa, aTy)
    for i in range(len(c)):
        print(f"c[{i}] = {c[i]}")

    def model(c, x):
        return c[0] + c[1]*x + c[2]*x**2

    r = A@c - y
    MKfel = sum(r**2)
    print(f'MK-fel: {MKfel}')
    # Plotta

    xfine = np.linspace(x[0],x[-1], num=1000)
    yfine = model(c,xfine)

    # Plotta data och rät linje
    plt.plot(x, y, 'o', label='Data', markersize=10)
    plt.plot(xfine, yfine, 'r', label='Anpassad rät linje')
    # Plotta avstånden mellan den räta linjen och data
    plt.plot([x[0], x[0]], [y[0], y[0]+r[0]],'g',label='Residual r[0]', markersize=10)
    plt.plot([x[1], x[1]], [y[1], y[1]+r[1]],'y',label='Residual r[1]', markersize=10)
    plt.plot([x[2], x[2]], [y[2], y[2]+r[2]],'k',label='Residual r[2]', markersize=10)
    plt.plot([x[3], x[3]], [y[3], y[3]+r[3]],'m',label='Residual r[3]', markersize=10)
    plt.plot([x[4], x[4]], [y[4], y[4]+r[4]],'c',label='Residual r[4]', markersize=10)
    plt.legend()
    plt.show()    

# Del d)
def MK_ansats_tredgerad():
    x = np.array([4, 5, 6, 7, 8])
    y = np.array([871, 1021, 1109, 1066, 929])

    ones = np.ones(np.shape(x))
    A = np.array([ones, x, x**2, x**3]).T
    print(A)
    aTa = A.T @ A
    aTy = A.T @ y
    c = np.linalg.solve(aTa, aTy)
    for i in range(len(c)):
        print(f"c[{i}] = {c[i]}")

    def model(c, x):
        return c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3     
    
    r = A@c - y
    MKfel = sum(r**2)
    print(f'MK-fel: {MKfel}')
    # Plotta

    xfine = np.linspace(x[0],x[-1], num=1000)
    yfine = model(c,xfine)

    # Plotta data och rät linje
    plt.plot(x, y, 'o', label='Data', markersize=10)
    plt.plot(xfine, yfine, 'r', label='Anpassad rät linje')
    # Plotta avstånden mellan den räta linjen och data
    plt.plot([x[0], x[0]], [y[0], y[0]+r[0]],'g',label='Residual r[0]', markersize=10)
    plt.plot([x[1], x[1]], [y[1], y[1]+r[1]],'y',label='Residual r[1]', markersize=10)
    plt.plot([x[2], x[2]], [y[2], y[2]+r[2]],'k',label='Residual r[2]', markersize=10)
    plt.plot([x[3], x[3]], [y[3], y[3]+r[3]],'m',label='Residual r[3]', markersize=10)
    plt.plot([x[4], x[4]], [y[4], y[4]+r[4]],'c',label='Residual r[4]', markersize=10)
    plt.legend()
    plt.show()  

# Del e)
def MK_ansats_trig():
    x = np.array([4, 5, 6, 7, 8])
    y = np.array([871, 1021, 1109, 1066, 929])
    ones = np.ones(np.shape(x))
    w = 2*np.pi/12

    A = np.array([ones, np.cos(w*x), np.sin(w*x)]).T
    print(A)

    aTa = A.T @ A
    aTy = A.T @ y
    c = np.linalg.solve(aTa, aTy)
    for i in range(len(c)):
        print(f"c[{i}] = {c[i]}")

    def model(c, x, w):
        return c[0] + c[1]*np.cos(w*x) + c[2]*np.sin(w*x)
    
    r = A@c - y
    MKfel = sum(r**2)

    print(f"MK-fel: {MKfel}")

    xfine = np.linspace(x[0], x[-1], num=1000)
    yfine = model(c, xfine, w)
    plt.plot(x, y, 'o', label='Data', markersize=10)
    plt.plot(xfine, yfine, 'r', label='Anpassad rät linje')
    plt.plot([x[0], x[0]], [y[0], y[0]+r[0]],'g',label='Residual r[0]', markersize=10)
    plt.plot([x[1], x[1]], [y[1], y[1]+r[1]],'y',label='Residual r[1]', markersize=10)
    plt.plot([x[2], x[2]], [y[2], y[2]+r[2]],'k',label='Residual r[2]', markersize=10)
    plt.plot([x[3], x[3]], [y[3], y[3]+r[3]],'m',label='Residual r[3]', markersize=10)
    plt.plot([x[4], x[4]], [y[4], y[4]+r[4]],'c',label='Residual r[4]', markersize=10)
    plt.legend()
    plt.show()



while True: 
    chois = int(input("Choose method to run (1-6) or any other key to exit:\n1. Naiv ansats\n2. Newton ansats\n3. Centrerad ansats\n4. MK ansats\n5. MK ansats tredgerad\n6. MK ansats trigonometrisk\n"))
    if chois == 1:
        naiv_ansats()
    elif chois == 2:
        newton_ansats()
    elif chois == 3:
        centrerad_ansats()
    elif chois == 4:
        MK_ansats()
    elif chois == 5:
        MK_ansats_tredgerad()
    elif chois == 6:
        MK_ansats_trig()
    else:
        break