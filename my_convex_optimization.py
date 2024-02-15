import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from scipy.optimize import linprog

def print_a_function(f, values):
    x = values
    y = f(x)
    plt.plot(x, y)

def find_root_bisection(f, min, max):
    c = (min + max) / 2
    while abs(max - min) > 0.001:
        if f(min) * f(c) > 0:
            min = c
        else:
            max = c
        c = (min + max) / 2
    return c

def find_root_newton_raphson(f, f_deriv, x):
    for i in range(100):
        if abs(f(x)) < 0.001:
            return x
        x = x - f(x) / f_deriv(x)
    return None

def gradient_descent(f, f_prime, start, learning_rate=0.1):
    for i in range(100):
        start = start - learning_rate * f_prime(start)
    return start

def solve_linear_problem(A, b, c):
    res = linprog(c, A_ub=A, b_ub=b, method="simplex")
    return res.fun, res.x

# Usage:

# Define the function
f = lambda x: (x - 1) ** 4 + x ** 2
f_prime = lambda x: 4 * ((x - 1) ** 3) + 2 * x

# Plot the function
values = np.linspace(-2, 3, 100)
print_a_function(f, values)

# Find the root using the bisection method
root_bisection = find_root_bisection(f, -2, 3)
print("Root (Bisection Method): {:.2f}".format(root_bisection))

# Find the root using Newton-Raphson method
initial_guess = 0.0  # Choose an appropriate initial guess closer to the root
root_newton_raphson = find_root_newton_raphson(f, f_prime, initial_guess)
if root_newton_raphson is not None:
    print("Root (Newton-Raphson Method): {:.2f}".format(root_newton_raphson))
else:
    print("Root (Newton-Raphson Method): No valid result")


# Use gradient descent to find the minimum
start_point = -1
min_point = gradient_descent(f, f_prime, start_point, 0.01)
print("Minimum (Gradient Descent): {:.2f}".format(min_point))

# Solve the linear problem using simplex method
A = np.array([[2, 1], [-4, 5], [1, -2]])
b = np.array([10, 8, 3])
c = np.array([-1, -2])

optimal_value, optimal_arg = solve_linear_problem(A, b, c)
print("Optimal Value: {:.2f}, Optimal Argument: {}".format(optimal_value, optimal_arg))
