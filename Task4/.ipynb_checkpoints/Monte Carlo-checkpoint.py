import numpy as np
from numpy import *

# Defining variables

fun = input("Enter a function f(x)=")
a = eval(input("Enter startpoint for integral:"))
b = eval(input("Enter endpoint for integral:"))
n = int(input("Enter number of points for integral:")) 
x = np.random.uniform(a, b, n)

# Evaluating users function

def f(x):
    return eval(fun)

# Computing integral

integral = ((b - a) / n)*np.sum(f(x))
print(f"Integral of {fun} from {a} to {b} with {n} points = {integral}")