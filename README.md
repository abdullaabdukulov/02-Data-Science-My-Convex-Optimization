# Welcome to My Convex Optimization

## Task
This project serves as an introduction to convex optimization tools and the implementation of root-finding algorithms. 
The primary focus is on optimizing a simple function and utilizing various root-finding methods and gradient descent 
for optimization.
<img src="https://storage.googleapis.com/qwasar-public/track-ds/convex_vs_non_convex.png" width="400">


## Description
    - def print_a_function(f, values)
    It will plot the function with the values received as parameters.



    def find_root_bisection(f, min, max)
    It will return the zero of a function using simple dichotomous algorithm between min and max for the function f.

    

    def find_root_newton_raphson(f, f_deriv)
    It will return the zero of a function using the Newton-Raphson's method between min and max for the function f.

<img src="https://storage.googleapis.com/qwasar-public/track-ds/brent_example.png" width="300" height="300">

    def gradient_descent(f, f_prime, start, learning_rate = 0.1)
    Write a simple gradient descent function which finds the minimum of a function f

<p><img src="https://storage.googleapis.com/qwasar-public/gradient_descent.png" width="300" height="300"> </p>
<<<<<<< Abdumalikov_Aziz


    def solve_linear_problem(A, b, c):
    Write a function solving the linear problem using simplex method. (see the first part to have more details)
    A = np.array([[2,1],[-4,5],[1,-2]])
    b = np.array([10,8,3])
    c = np.array([-1,-2])


## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/aabdumalikov/02-Data-Science-My-Convex-Optimization.git
   ```

2. Navigate to the project directory:

    ```bash
    cd 02-Data-Science-My-Convex-Optimization
    ```

3. Install required dependencies:

    ```bash
    pip install numpy matplotlib scipy
    ```

## Usage
1. Open the main.py file in your preferred Python environment.
2. Run the jupyter.

    ```bash
    python my_convex_optimization.ipynb
    ```

The script will execute and provide outputs for root-finding, optimization using gradient descent, and solving a linear problem.









=
