import numpy as np
from math import log

# Using numpy ufuncs to perform element-wise operations on arrays
# Example: Adding two arrays element-wise
x= [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z  =np.add(x, y)
print(z)

#to create our own ufunc
def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd,2,1) # 2 inputs, 1 output
x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])
z = myadd(x, y)
print("The result of myadd is:")
print(z)

#check if function is a ufunc
print(type(np.add))  # <class 'numpy.ufunc'>
print(type(myadd))  # <class 'numpy.ufunc'>

print(type(np.concatenate))


#use if statement to check if a function is a ufunc
if type(np.add)== np.ufunc:
    print("add is a ufunc")
else:
    print("add is not a ufunc")

#simple arthematic ufuncs
print("\n Simple arithmetic ufuncs:")

#addition
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
new_arr = np.add(arr1, arr2)
print("Addition result:")
print(new_arr)
#subtraction
new_arr = np.subtract(arr1, arr2)
print("Subtraction result:")
print(new_arr)
#multiplication
new_arr = np.multiply(arr1,arr2)
print("Multiplication result:")
print(new_arr)
#division
new_arr = np.divide(arr1,arr2)
print("Division result:")
print(new_arr)

#power
new_arr = np.power(arr1, 2)
print("Power result:")
print(new_arr)
#Remainder
reminder = np.remainder(arr1, 2)
print("Remainder result:")
print(reminder)
#mode
mode = np.mod(arr1, 2)
print(mode)


#quotienT and Mod 
new_arr = np.divmod(arr1, 2)
print("Quotient and Mod result:")
print(new_arr)

#absolute value
arr1 = np.array([-10, -11, -12, -13, -14, -15])
abs_arr = np.absolute(arr1)
print("Absolute value result:")
print(abs_arr)

#Ufunc Rounding Decimals
#Truncation
arr = np.trunc([-3.43, 3.666])
print("Truncated array:")
print(arr)
#fix
arr = np.fix([-3.143, 3.666])
print("Fixed array:")
print(arr)

#Rounding 
arr = np.round([-3.143, 3.666])
print("Rounded array:")
print(arr)
#Rounding to 2 decimal places
arr = np.around([-3.143, 3.666],2)
print("Rounded to 2 decimal places:")
print(arr)


# floor 
arr = np.floor([-3.1,3.5,3.6,-3.8])
print("Floor result:")
print(arr)

#ceil

arr = np.ceil([-3.1,3.5,3.6,-3.8])
print("Ceil result:")
print(arr)

# Numpy Logs
print("\n Numpy Logs:")
#log2
arr = np.arange(1,10)
print("Original array:")
print(arr)
print("Log2 result:")
print(np.log2(arr))

#log base 10
print("Log10 result:")
print(np.log10(arr))

#log base e or natural log
print("Natural log result:")
print(np.log(arr))

#log at any base

nplog = np.frompyfunc(log,2,1)  # 2 inputs, 1 output
# Example usage of nplog
print("Log base 100 of 15:")
print(nplog(100, 15))

#Numpy Ufunc Summations
# add
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
new_arr = np.add(arr1, arr2)
print("Addition result:")   
print(new_arr)

# sum
new_arr = np.sum([arr1, arr2])
print("Sum:")   
print(new_arr)
#  summition over axis
new_arr  = np.sum([arr1, arr2], axis=1)
print("Sum over axis 1:")
print(new_arr)

#cummulative sum
new_arr = np.cumsum([arr1])
print("Cumulative sum:")
print(new_arr)

#Ufunc Product
# prod
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
new_arr = np.prod([arr1])
print("Product result:")    
print(new_arr)

#product of two arrays
new_arr = np.prod([arr1, arr2])
print("Product of two arrays:") 
print(new_arr)

#PRODUCT OVER AXIS
new_arr = np.prod([arr1, arr2], axis=1)
print("Product over axis 1:")
print(new_arr)

#cummulative product
new_arr = np.cumprod([arr1])    
print("Cumulative product:")
print(new_arr)

# numpy_ufuncs Differences 
#diff()

arr = np.array([10, 15, 25, 5, ])
new_arr = np.diff(arr)
print("difference between consecutive elements:")
print(new_arr)

#diff with n=2
new_arr  = np.diff(arr, n=2)
print("Difference with n=2:")
print(new_arr)


# LCM 
print("\nLCM:")
n1 = 6
n2 = 4
lcm = np.lcm(n1, n2)
print(f"LCM of {n1} and {n2} is: {lcm}")
arr1 = np.array([10, 15, 25, 5])
x = np.lcm.reduce(arr1)
print(f"LCM of array {arr1} is: {x}")


# Find the LCM of all values of an array where the array contains all integers from 1 to 10:
arr = np.arange(1,11)
x = np.lcm.reduce(arr)
print(f"LCM of all integers from 1 to 10 is: {x}")


#HCF GCD
print("\nHCF GCD:")
n1=6
n2=9

x = np.gcd(n1, n2)
print(f"GCD of {n1} and {n2} is: {x}")


#finding GCF in array
arr1 = np.array([10, 15, 25, 5])
x= np.gcd.reduce(arr1)
print(f"GCD of array {arr1} is: {x}")


#Trignometric Functions
print("\nTrigonometric Functions:")
# Sine
x = np.sin(np.pi / 2)
print(f"Sine of pi/2: {x}")

arr = np.array([0, np.pi / 2, np.pi])
x = np.sin(arr)
print("Sine of array [0, pi/2, pi]:")
print(x)

#convert degree into radians
arr = np.array([0, 30, 45, 60, 90])
x = np.deg2rad(arr)
print("Degrees to Radians:")
print(x)

#Radians to Degrees
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print("Radians to Degrees:")
print(x)

#inverse of sine cosine and tangent
print("\nInverse Trigonometric Functions:")
# Inverse Sine
x = np.arcsin(1)
print(f"Inverse Sine of 1: {x}")
# Inverse Cosine
x = np.arccos(0)
print(f"Inverse Cosine of 0: {x}")
# Inverse Tangent   
x = np.arctan(1)
print(f"Inverse Tangent of 1: {x}")

# angle of each value in array
arr = np.array([1, -1, 0.1])
x = np.arctan(arr)
print("Inverse Tangent of array :")
print(x)

# hypotenuse
print("\nHypotenuse:")
base = 3
perp = 4

x = np.hypot(base, perp)
print(x)

## Numpy Set Operations
print("\nNumpy Set Operations:")


# creating a set 
arr = np.array([1, 2, 3, 4,3,4,5,6,7,8,4,3,2,5])
x =np.unique(arr)
print(x)
