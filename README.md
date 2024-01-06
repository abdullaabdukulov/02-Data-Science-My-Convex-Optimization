# Welcome to My Convex Optimization
To get a feel with the problem, we are going to start with a simple function to optimize:

f(x) = (x - 1)^4 + x^2

Which translates in python to: f = lambda x : (x - 1)**4 + x**2



## Task
Intuitively, the measure of 'how far' is our model prediction from the correct answer tells us about the effectiveness of our algorithm. The farther is our prediction the worse is our performance. We can then define a cost function based on this 'distance'. We want to minimize this cost function in order to have the best prediction possible, i.e we want to find the point where the value of this cost function is the lowest.

## Description
On the left, the function is said to be convex: it is beautifully round. On the contrary, the function on the right has a lot of valleys and bumps.
The minimum of the convex function is much easier to reach: we just need to follow the slope ! With non convex function, following the slope would not work since reaching a cavity does not ensure that this cavity is the lowest one !

## Installation
- pip install matplotlib
- pip install numpy
- pip install scipy

## Usage
```
python ./my_convex_optimization
```
At the bottom of the code added how to use the code.

### The Core Team
