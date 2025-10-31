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

#naiv_ansats()

# Newtons method for polynomial fitting
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
    
    # Evaluera polynom i många punkter för plot
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


#newton_ansats()

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

        def pol_centrerad(c, x, t_mean):
            return sum(c[i] * (x - x_mean)**i for i in range(len(c)))

    # Rita ut
    x_smooth = np.linspace(x[0], x[-1], 300)
    y_smooth = pol_centrerad(c, x_smooth, x_mean)

    plt.plot(x, y, 'bo', label='Datapunkter')
    plt.plot(x_smooth, y_smooth, 'r-', label='Centrerad ansats')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Polynominterpolation - Centrerad ansats')
    plt.legend()
    plt.grid(True)
    plt.show()
        


centrerad_ansats()