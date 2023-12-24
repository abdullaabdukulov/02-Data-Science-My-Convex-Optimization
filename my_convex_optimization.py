import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

def print_a_function(f, values):
    x = np.linspace(min(values), max(values), 100)
    y = [f(val) for val in x]

    plt.plot(x, y, label='f(x)')
    plt.scatter(values, [f(val) for val in values], color='red', marker='x', label='f')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.savefig('my_plot_journey.png')
    plt.grid(True)
    plt.show()
    
def find_root_bisection(f, min, max):
    while (max - min) > 0.001:
        mid = (min + max) / 2
        if f(mid) == 0:
            return mid
        elif f(min) * f(mid) < 0:
            max = mid
        else:
            min = mid
    return (min + max) / 2

def find_root_newton_raphson(f, f_deriv, x0, precision=0.001):
    x = x0
    while abs(f(x)) > precision:
        x = x - f(x) / f_deriv(x)
    return x

def gradient_descent(f, f_prime, start, learning_rate=0.1):
    x = start
    for _ in range(200):
        x = x - learning_rate * f_prime(x)
    return x


def solve_linear_problem(A, b, c):
    result = linprog(c, A_ub=A, b_ub=b)
    return round(result.fun), result.x