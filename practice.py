from math import sqrt, log
from matplotlib import pyplot as plt

f = lambda t, x: t**2*sqrt(x**2 + t**2)
_F = lambda t, x: x*sqrt(t**2 + x**2)*(2*t**3+t*x**2)/abs(x)/8 - x**4*log(abs(x*sqrt(t**2+x**2)+t*abs(x)))/8
F = lambda t, x: _F(t, x) if x != 0 else _F(t, 10E-20)
delta = lambda pair: abs(pair[0] - pair[1])

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))
N = int(input("Введите N: "))

X = [c + i * (d-c) / 20 for i in range(21)]
h = (b-a) / N
T = [a + i * h for i in range(N + 1)]
Iapproximate = [h * sum([(f(T[i - 1], x) + f(T[i], x)) / 2 for i in range(1, N + 1)]) for x in X]
Iaccurate = [F(b, x) - F(a, x) for x in X]
print("Максимальная невязка: {}".format(max(list(map(delta, list(zip(Iapproximate, Iaccurate)))))))

plt.title("Графики значений определенного интеграла при X от {} до {}".format(c, d))
plt.ylabel("Значение определенного интеграла")
plt.xlabel("Значение X")
plt.grid(True)
plt.plot(X, Iaccurate, color="green", label="Точное")
plt.plot(X, Iapproximate, color="red", label="Приближенное")
plt.legend()
plt.show()
