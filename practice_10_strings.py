from math import sqrt, log
from matplotlib import pyplot as plt
f, delta = lambda t, x: (t**2)*sqrt(x**2 + t**2), lambda a: abs(a[0]-a[1]) #Подынтегральная функция
def F(t, x):
    t = t if t != 0 else 10E-20
    x = x if x != 0 else 10E-20
    return x*sqrt(t**2 + x**2)*(2*t**3+t*x**2)/abs(x)/8 - x**4*log(abs(x*sqrt(t**2+x**2)+t*abs(x)))/8
a, b, c, d, N = float(input("Введите a: ")), float(input("Введите b: ")), float(input("Введите c: ")), float(input("Введите d: ")), int(input("Введите N: "))
Iapproximate, Iaccurate = [((b-a)/N) * sum([sum([f(t, x) for t in [a + i*(b-a)/N for i in range(N+1)][k-1:k+1]])/2 for k in range(1, N+1)]) for x in [c + i*(d-c)/20 for i in range(21)]], [F(b,x) - F(a, x) for x in [c + i*(d-c)/20 for i in range(21)]]
_, _, _, _ = print("Max невязка: {}".format(max(list(map(delta, list(zip(Iapproximate, Iaccurate))))))), plt.plot(Iaccurate, color="green"), plt.plot(Iapproximate, color="red"), plt.show()
