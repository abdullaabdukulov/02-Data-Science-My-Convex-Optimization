# Description

One of the main challenges of Data Science and more specifically in Machine Learning is the performance measure. How to measure performance efficiently so that our model predictions meet the business objectives?

For example, let's pretend our goal is to classify fruits to know if a fruit is an apple, an orange, or something else, depending on some attributes (color, shape, weight...).

Intuitively, the measure of 'how far' is our model prediction from the correct answer tells us about the effectiveness of our algorithm. The farther is our prediction the worse is our performance. We can then define a cost function based on this 'distance'. We want to minimize this cost function in order to have the best prediction possible, i.e we want to find the point where the value of this cost function is the lowest.

Generally, minimizing a function is not an easy task. However, some functions are easier to optimize than others: Convex functions.

# Task

To get a feel with the problem, we are going to start with a simple function to optimize:

f(x) = (x - 1)^4 + x^2

Which translates in python to: f = lambda x : (x - 1)**4 + x**2

→ Plot this function to get a feel of what it looks like !

To find the minimum of our little f function, we are going to use its derivative f' (f prime). The zero of f prime (the point where it evaluates to zero) matches with the minimum of the f function.

Our goal is hence to find where f prime cancels out.

→ Write a simple dichotomous algorithm (bisection method) to find the zero of a function.

def find_root(f, a, b) should returns x such that f(x) = 0. Since computers only understand discrete value, we will have a precision of 0.001, i.e find x such that |f(x)| < 0.001 (|.| is the absolute value function).

If your dichotomous find_root function works well, you can try other root-finding algorithms like Newton-Raphson's or Muller's method (but they are many more).

Once you are done playing around with root-finding methods, we will use find_root to find the minimum of f. As explained above, the root of f', the derivative of f, is where f reaches its minimum.

→ Use find_root to find the root of f prime.

f' = 4*(x - 1)^3 + 2x

To make sure the answer is correct, we will check it against Brent's method for optimization. Brent's method works as a combination of the secant method and parabola fittings.

# Installation
pip install matplotlib
pip install numpy
pip install scipy

# Usage
python3 my_convex_optimization.py