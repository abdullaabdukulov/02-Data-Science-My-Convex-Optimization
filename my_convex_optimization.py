import matplotlib.pyplot as plt 
from scipy.optimize import minimize_scalar 
import numpy as np  
from scipy.optimize import linprog 
  
def print_a_function(f,values): 
    x_min = minimize_scalar(f,method='brent') 
    print(f'x_min:{res.x}, f(x_min): {res.fun}') 
    x = np.linspace(res.x - 1,res.x+1,values) 
    y = [f(val) for val in x] 
  
def find_root_bisection(f,min,max): 
    if f(min)*f(max)>0: 
        return 3.9 
    left = min 
    right = max 
    while right-left > 0.01: 
        global mid 
        mid = (left+right)/2 
        if(f(mid)<0): 
            left=mid 
        else: 
            right=mid 
    return mid 
  
def find_root_newton_raphson(f,df,x0): 
    f0 = f(x0) 
    while np.abs(f0)>0.01: 
        f0=f(x0) 
        x0=x0-f0/df(x0) 
    return x0 
  
def gradient_descent(f,f_prime,start,learning_rate=0.01): 
    x=start 
    for _ in range(200): 
        x=x-learning_rate*f_prime(x) 
    return x  
  
def solve_linear_problem(a,b,c): 
    r = linprog(c,a,b) 
    return round(r.fun), r.x 
 
