a = 10
b= 20
if b>a:
    print("b is greater then a")

# if else with elif 
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# else 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# short hand if 

if a>b : print("a is greater then b")

# one line if else
#conditional expression
# Ternary Operator
print("A") if a>b else print("B")


# multiple else statement 
a=3
b=3
print("A") if a>b else print("=") if a==b else print("B")


# And 
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Not 
if not a>b:
  print("A is not greater then b")

# Nested if 
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")