#function defination
def my_function():
    print("Hello from Function")
#function call 
my_function()

# funciton with arguments 
def my_fuction1(fname):
    print(fname+ " Refsense")

my_fuction1("Email")

# arbitrary Arguments *arg

def my_fun(*kids):
    print("the youngus child is " + kids[1])

my_fun("ali", "hamza", "adnan")


## keyword argument
def my_function2(child1,child2, child3):
    print("The  youngest child is " +child1)
my_function2(child1="ali", child2="hamza", child3="rehman")

# arbitray keywords  **kward
def my_function(**kid):
  print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")


#  default value 
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# passing a list to a funciton 

def list_fun(food):
   for x in food:
      print(x)

fruits = ["apple", "banana", "cherry"]
list_fun(fruits)

# return Value
def my_func(x):
   return x*3
print(my_func(4))

# positional argumets
def my_fun(x, /):
   print(x)
my_fun(5)

# keyword only arguments 
def my_fun(*,x):
   print(x)
my_fun(x=3)


#Recursion Functions

def tri_recursion(k):
   if(k>0):
      result = k +tri_recursion(k-1)
      print(result)
   else:
      result=0
   return result

print("Recursion Result examples")
tri_recursion(6)



### Lambda Funcitons 

# syntax 
# lambda arguments : expression
print("\n Lmadba Functions Call")
x  = lambda a: a+10
print(x(5))

#two numbers aurguments
x= lambda a, b: a*b
print(x(5,6))

# lambda is more powerfull when it is used inside a function
def myfun(n):
   return lambda a: a*n
x = myfun(3)
print(x(11))






    