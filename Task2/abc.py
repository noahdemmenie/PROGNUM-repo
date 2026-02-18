from math import sqrt

# Coefficients of the quadratic equation

a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

# Compute discriminant

D = b**2-4*a*c

if D > 0:
    # Two real solutions
    x1 = (-b+sqrt(D))/(2*a)
    x2 = (-b-sqrt(D))/(2*a)
    print(f"The solutions are x1 = {x1} and x2 = {x2}")
elif D == 0:
    # One real solution
    x1 = (-b+sqrt(D))/(2*a)
    print(f"The solution is x = {x1}")
else:
    # No real solution if D < 0
    print("No solutions could be found")