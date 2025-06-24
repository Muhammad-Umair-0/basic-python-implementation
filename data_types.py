x= 5
print(type(x))
# list data type 
x1 = ["apple", "banana", "cherry"]
print(type(x1))


# we can set  specific data type 
# for string
X = str("hello word")

#integer
y= int(20)

print(type(x),type(y))

#float
a = float(20.5)

b= complex(1j)

print(type(b))


## actual Values
x= 1 #int
y = 2.5  #float
z = 1j  #complex
# conersion 
a = float(x)
b = int(y)
c = complex(x)


# check data types
print(a, type(a))
print(b,(type(b)))
print(c, type(c))



## random numbers 
import random
print(random.randrange(1,12))