# Welcome to My-Convex-Optimization

<h3>Task</h3>
<img src="https://storage.googleapis.com/qwasar-public/track-ds/convex_vs_non_convex.png" width="400">
<p>To get a feel with the problem, we are going to start with a simple function to optimize:</p>
<p><code>f(x) = (x - 1)^4 + x^2</code></p>
<p>Which translates in python to: <code>f = lambda x : (x - 1)**4 + x**2</code></p>
<p>→ <strong>Plot this function to get a feel of what it looks like !</strong></p>
<p>To find the minimum of our little f function, we are going to use its derivative f' (f prime). The zero of f prime (the point where it evaluates to zero) matches with the minimum of the f function.</p>
<p>Our goal is hence to find where f prime cancels out.</p>
<p>→ <strong>Write a simple dichotomous algorithm (bisection method) to find the zero of a function</strong>.</p>
<p><code>def find_root(f, a, b)</code> should returns x such that f(x) = 0. Since computers only understand discrete value, we will have a precision of <strong>0.001</strong>, i.e find x such that |f(x)| &lt; 0.001 (|.| is the absolute value function).</p>
<p>If your dichotomous find_root function works well, you can try other root-finding algorithms like Newton-Raphson's or Muller's method (but they are many more).</p>
<p>Once you are done playing around with root-finding methods, we will use find_root to find the minimum of f. As explained above, the root of <strong>f'</strong>, the derivative of f, is where f reaches its minimum.</p>
<p>→ <strong>Use find_root to find the root of f prime.</strong></p>
<p><code>f' = 4*(x - 1)^3 + 2x</code></p>
<p>To make sure the answer is correct, we will check it against Brent's method for optimization. Brent's method works as a combination of the secant method and parabola fittings.</p>
<pre class=" language-plain"><code class=" language-plain">import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar

res = minimize_scalar(f, method='brent')
print('x_min: .02f, f(x_min): .02f'  (res.x, res.fun))

# plot curve
x = np.linspace(res.x - 1, res.x + 1, 100)
y = [f(val) for val in x]
plt.plot(x, y, color='blue', label='f')

# plot optima
plt.scatter(res.x, res.fun, color='red', marker='x', label='Minimum')

plt.grid()
plt.legend(loc = 1)
</code></pre>
<p>You should see something similar to:</p>
<img src="https://storage.googleapis.com/qwasar-public/track-ds/brent_example.png" width="300" height="300">
<h4>Gradient Descent Methods</h4>
<p>Suppose you are lost at the top of a hill at night. You cannot see anything, you can only feel the ground beneath your feet. An intuitive way to reach the village downhill as fast as possible is to follow the steepest slope.</p>
<p>This is the idea behind the gradient descent. It measures the local gradient of the cost function and goes towards the direction of the descending gradient. Once the gradient cancels out, it means we reached a minimum.</p>
<p>x<sub>k + 1</sub> = x<sub>k</sub> - α ∇f(x<sub>k</sub>)</p>
<p>where ∇f is the gradient of f and α is called the <strong>learning rate</strong>. This is how big you step towards the direction of the descending gradient.</p>
<p>In our one dimension example, the gradient of f is simply the derivative of f.</p>
<p>Here is an example in 3D:</p>
<p><img src="https://storage.googleapis.com/qwasar-public/gradient_descent.png" width="300" height="300"> </p>
<p>→ <strong>How does the learning rate influence the efficiency of the algorithm? What happens if it is very small? What if it is very big?</strong></p>
<p>→ <strong>Write a simple gradient descent function which finds the minimum of a function f</strong></p>
<p>Similarly, we will stop our search with a precision of 0.001.</p>
<pre class=" language-plain"><code class=" language-plain">def gradient_descent(f, f_prime, start, learning_rate = 0.1)
    ...


f = lambda x : (x - 1) ** 4 + x ** 2
f_prime = lambda x : 4*((x-1)**3) + 2*x
start = -1
x_min = gradient_descent(f, f_prime, start, 0.01)
f_min = f(x_min)

print("xmin: 0.2f, f(x_min): 0.2f"  (x_min, f_min))

</code></pre>
<p>Is the result similar to the previous Brent's method?</p>
<p>Using the gradient_descent, you should find a value similar to the previous methods.</p>
<p>Gradient Descent methods are the workhorse of machine learning, from linear regression to deep neural nets.
Here, we used it in a one dimension problem, but it can be used with any number of dimensions !</p>
<h4>To go further</h4>
<p>Adding linear constraints to a convex function does not change its convexity, it remains convex. What it does though is restricting the space of solutions by intersecting it with hyperplanes.
If our convex function solution space is a spherical orange, applying linear constraints is like slicing the orange. It remains convex but sharper.</p>
<p><img src="https://storage.googleapis.com/qwasar-public/track-ds/linear_constraints_orange.png" width="200" height="200"></p>
<p>More specifically, let us consider the following <a href="https://en.wikipedia.org/wiki/Linear_programming" target="_blank">linear problem</a> with two variables:</p>
<p>maximize   z = x + 2y
subject to
      • 2x + y ≤ 10
      • -4x + 5y ≤ 8
      • x - 2y ≤ 3
      • x, y ≥ 0</p>
<p>Which can be rewritten as:</p>
<p>maximize   z = c<sup>T</sup>·x
subject to
      • Ax ≤ b
      • x ≥ 0</p>
<p>z is called the objective function, A a coefficients matrix, and b the non-negative constraints. The space defined by the constraints equations is called the <strong>feasible region</strong>.
This is a convex polytope. It can be shown that so solutions which maximizes the objective function are located on the vertices of this polytope.</p>
<img src="https://storage.googleapis.com/qwasar-public/track-ds/polytope_example_drawn.png" width="350" height="350">
<p>On the picture, we can visualize the feasible region in beige in the middle. The red line represents the function 2x +y = 10, the white one -4x +5y = 8 and blue one represents
the function x - 2y = 3. The area inside the orange polytope is the intersection between all the constraints inequalities.</p>
<p>→ <strong>Initialize A, b, and c as numpy arrays</strong></p>
<pre class=" language-plain"><code class=" language-plain">A = ...
b = ...
c = ...
</code></pre>
<h4>Simplex algorithm</h4>
<p>We are going to solve this linear problem with the <a href="https://en.wikipedia.org/wiki/Simplex_algorithm" target="_blank">Simplex method</a>.
The simplex algorithm is pretty straightforward: it moves from a vertex to another until it finds a solution which maximizes the objective function.</p>
<p>→ <strong>Solve the linear problem using simplex method</strong></p>
<p><strong>hint</strong>: You can use <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html" target="_blank">scipy's implementation of Simplex</a>.</p>
<pre class=" language-plain"><code class=" language-plain">def solve_linear_problem(A, b, c):
	...

optimal_value, optimal_arg = solve_linear_problem(A, b, c)

print("The optimal value is: ", optimal_value, " and is reached for x = ", optimal_arg)

</code></pre>
<p>→ <strong>Is the solution you found located on the edge of the polytope? Why?</strong></p>
<p><strong>hint</strong>: The idea is very similar to the <a href="https://en.wikipedia.org/wiki/Gaussian_elimination" target="_blank">Gauss' pivot</a></p>
<h3>Description</h3>
<p>You will have to implement multiple functions:</p>
<pre class=" language-plain"><code class=" language-plain">- def print_a_function(f, values)
It will plot the function with the values received as parameters.

- def find_root_bisection(f, min, max)
It will return the zero of a function using simple dichotomous algorithm between min and max for the function f.

- def find_root_newton_raphson(f, f_deriv)
It will return the zero of a function using the Newton-Raphson's method between min and max for the function f.

- def gradient_descent(f, f_prime, start, learning_rate = 0.1)
Write a simple gradient descent function which finds the minimum of a function f

- def solve_linear_problem(A, b, c):
Write a function solving the linear problem using simplex method. (see the first part to have more details)
A = np.array([[2,1],[-4,5],[1,-2]])
b = np.array([10,8,3])
c = np.array([-1,-2])
</code></pre>

### Installation
For working with this project you should install required libraries mentioned in `requirements.txt` file. do this instead:
```pip install -r requirements.txt```

### Usage
for using this project you need to run `my_convex_optimization.ipynb` file