from numpy import sin, cos, exp, pi
import numpy as np
from scipy import integrate

# Users input function

while True:
    fun = input("Enter function f(x): ")
    fun = fun.replace("^", "**") # If user types ^ instead of **, it will replace it so that it still works.

    try:
        x = 1  # Give x a temporary value for a test
        test = eval(fun)  # Test to see if users function works
        del x  # Delete the temporary x value to prevent problems in output

        if callable(test):
            raise TypeError  # If user types sin instead of sin(x) for example, it will give a TypeError. Without this, the TypeError doesnt work or it works when I put the type error exception in the loop for integration but then it will give a TypeError after the user types bounds, which is weird.

        f = lambda x: eval(fun) # Evaluate users function
        break

    except NameError:
        print("NameError: You used something undefined, forgot a mathematical sign perhaps? (allowed, something with x, sin(x), cos(x), exp(x), pi or any real number).")

    except TypeError:
        print("TypeError: Function must depend on x (e.g. sin(x), not sin).")

    except SyntaxError:
        print("SyntaxError: Invalid expression, forgot a mathematical sign and/or variable perhaps?")

# Users input bounds

while True:
    try:
        a = eval(input("Enter lower bound for integral: "))
        break

    except NameError:
        print("NameError: Bound must be a real number.")

    except SyntaxError:
        print("SyntaxError: Invalid expression, typo or forgot a mathematical sign perhaps?")

while True:
    try:
        b = eval(input("Enter upper bound for integral: "))
        break

    except NameError:
        print("NameError: Bound must be a real number.")

    except SyntaxError:
        print("SyntaxError: Invalid expression, typo or forgot a mathematical sign perhaps?")

# Compute users integral

while True:
    try:
        integral_quad = integrate.quad(f, a, b)[0]
        print(f"Integral of {fun} from {a} to {b} with quad() = {integral_quad}")
        break

    except ZeroDivisionError:
        print("ZeroDivisionError: Division by zero during integration.")

    except ValueError:
        print("ValueError: Invalid value during integration.")

# Define given function

f_mc = lambda x: x**4+exp(sin(x)+cos(x))

# Compute integral of given function from 0 to pi with quad()

a = 0
b = pi

integral_quad = integrate.quad(f_mc, a, b)[0]
print(f"Integral of x^4+e^(sin(x)+cos(x)) from {a} to {b} with quad() = {integral_quad}")

# Compute integral of given function from 0 to pi with Monte Carlo

n = 1000000
x = np.random.uniform(a, b, n)
integral_mc = ((b - a) / n)*np.sum(f_mc(x))
print(f"Integral of x^4+e^(sin(x)+cos(x)) from {a} to {b} with Monte Carlo = {integral_mc}")