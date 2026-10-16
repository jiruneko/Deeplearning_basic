import numpy as np
import matplotlib.pyplot as plt

def function_1(x):
    return 0.01 * x**2 + 0.1 * x

def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)

x = np.arange(0, 20.1, 0.1)
y = function_1(x)

# x = 5 における接線
a = numerical_diff(function_1, 5)
b = function_1(5) - a * 5

tangent = a * x + b

plt.plot(x, y, label="f(x)")
plt.plot(x, tangent, label="Tangent")
plt.scatter(5, function_1(5))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
