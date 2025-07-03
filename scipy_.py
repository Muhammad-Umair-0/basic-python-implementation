import scipy
from scipy import constants
from scipy.optimize import root
from math import cos
from scipy.optimize import minimize


print(constants.liter)

#checking scipy version 
print("the scipy version is")
print(scipy.__version__)

print(constants.pi)

print(dir(constants))


# Optimizers
#Find root of the equation x + cos(x)
def eqn(x):
    return x+cos(x)

myroot= root(eqn, 0)
print("optimizer")
print(myroot.x)


#find minimizing
# Minimize the function x^2 + x + 2 with BFGS:

def eqn(x):
    return x**2 + x+2


mymin = minimize(eqn, 0, method='BFGS')
print("\n the minimizer")
print(mymin)


# Sparse Data

