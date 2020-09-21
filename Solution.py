import math
import itertools

# data at the surface
def z_factor():
    """
    pres = p
    global temp
    temp = t
    global sg
    sg = sgi
    ppr = pres / ppci
    tpr = temp / tpci
    """
    densir = (0.27 * ppr) / tpr
    a1 = 0.3265
    a2 = -1.07
    a3 = -0.5339
    a4 = 0.01569
    a5 = -0.05165
    a6 = 0.5475
    a7 = -0.7361
    a8 = 0.1844
    a9 = 0.1056
    a10 = 0.6134
    a11 = 0.7210
    r1 = a1 + (a2 / tpr) + (a3 / (tpr ** 3)) + (a4 / (tpr ** 4)) + (a5 / (tpr ** 5))
    r2 = (0.27 * ppr) / tpr
    r3 = a6 + (a7 / tpr) + (a8 / (tpr ** 2))
    r4 = a9 * ((a7 / tpr) + (a8 / tpr ** 2))
    r5 = a10 / tpr ** 3
    densir = (0.27 * ppr) / (tpr)
    tim = math.exp(-a11 * (densir ** 2))

    def factor():
        fpr = 1 + (r1 * densir) - (r2 / densir) + (r3 * (densir ** 2)) - (r4 * (densir ** 5)) + (
                    r5 * (1 + (a11 * (densir ** 2)))) * tim

        fprime = r1 + (r2 / densir ** 2) + (2 * r3 * densir) - (5 * r4 * (densir ** 4)) + (2 * r5 * densir) * math.exp(
            (-a11 * densir ** 2) * ((1 + 2 * a11 * (densir ** 3)) - (a11 * (densir ** 2)) * (1 + a11 * (densir ** 2))))
        global hfac
        hfac = fpr / fprime
        global densir1
        densir1 = densir - hfac

    factor()
    while abs(hfac) >= 0.0000000000001:
        densir = densir1
        factor()
        continue
    global zfactor
    zfactor = ((0.27 * ppr) / (densir1 * tpr))*0.8775
def cullender_smith():
    global ppr
    ppr = whpres/ppci
    global tpr
    tpr = whtemp/tpci
    z_factor()
    z1 = zfactor
    p1 = whpres
    t1 = whtemp
    int1 = (1000*t1*z1)/p1
    intenew.append(int1)
    int2 = int1
    detap = (37.5*sgi*(depth/2))/(int1+int2)
    p2 = p1 + detap
    def interi():
        global ppr
        ppr = p2/ppci
        t2 = (t1 + bhtemp)/2
        global tpr
        tpr = t2/tpci
        z_factor()
        z2 = zfactor
        global int2i
        int2i = (1000*t2*z2)/p2
        detap = (37.5*sgi*(depth/2))/(int2i+int2)
        global p2i
        p2i = p1+detap
    interi()
    while p2i != p2 :
        p2 = p2i
        int2 = int2i
        interi()
        continue
    print(p2i, p2,int2i, "it's equal now")
    intenew.append(int2i)

    int3 = int2
    detap = (37.5 * sgi * (depth / 2)) / (int3 + int2)
    p3 = p2i + detap

    def downn():
        global ppr
        ppr = p3 / ppci
        t3 = bhtemp
        global tpr
        tpr = t3 / tpci
        z_factor()
        z3 = zfactor
        global int3i
        int3i = (1000 * t3 * z3) / p3
        detap = (37.5 * sgi * (depth / 2)) / (int3i + int3)
        global p3i
        p3i = p2i + detap

    downn()
    while p3i != p3:
        p3 = p3i
        int3 = int3i
        downn()
    print(p3i, p3, int3i, "it's equal now")
    intenew.append(int3i)
    pfinal = whpres + ((112.5*sgi*depth)/(intenew[0]+(4*intenew[1]+intenew[2])))

    print(pfinal)
global whtemp
whtemp = eval(input("Please input your wellhead temperature (degR): "))
global bhtemp
bhtemp = eval(input("Please input your temperature at the bottom (degR): "))
global whpres
whpres = eval(input("Please input your wellhead pressure (psia): "))
iniwhpres = whpres
global depth
depth  = eval(input("Please input your well depth: "))
step = depth/2
global sgi
sgi = eval(input("Please input your measured gas gravity: "))
global h2s
h2s  = eval(input("Please input the H2S concentration: "))
global co2
co2  = eval(input("Please input the CO2 concentration: "))
global n2
n2  = eval(input("Please input the N2 concentration: "))
if (h2s+co2+n2)<= 0.5:
    global tpci
    tpci = float(168 + 325 * sgi - 12.5 * sgi ** 2)
    global ppci
    ppci = float(677 + 15 * sgi - 37.5 * sgi ** 2)
else:
    tpci = float(tpci - 80*co2 + 130*h2s - 250*n2)
    ppci = float(ppci + 440*co2 + 600*h2s -170*n2)

print("gas gravity is: ", sgi)
print("Critical temperature = ", tpci)
print("Critical pressure= ", ppci)
intenew = []
