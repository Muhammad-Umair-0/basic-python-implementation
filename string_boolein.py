# define a string 
print("Meri_Tech")

#string to a Variable
a = "MEri_tech"
print(a)

# Multiline string 
a = """
Meri_Tech,
is a data driven organization,
we provide the soution to drive from data
"""
print(a)


#string array
a = "MEri_TeCh"
print(len(a))
print(a[8])


#LOOPing  Through string
for i in a:
    print(i, end="")

print("/n")


## check String 

text = "Meri_Tech,is a data driven organization,we provide the soution to drive from data"
print("Tech" in text)
#use if statement 
if "Tech" in text:
    print("Yes , 'Tech' is in text")


## cheak if  String not in Text
print("TExt" not in text)

# use if statement
if "TExt" not in text:
    print("'TExt' is not present")



## string slicing
print(a[2:6])

print(a[:5])

print(a[2:])

print(a[:-1])


## String modification 
#upper case
print(a.upper())

#lower case
print(a.lower())


# Remove white space
a = " Meri Tech "
print(a.strip())

#Replace String 
print(a.replace("e", "a"))

## split 
print(a.split(" "))


#String Concatenation 
a = "Meri"
b= "Tech"
c= a+b
print(c)



#To add space between them
c= a+" "+b
print(c)

#as we know we cannot add int or float directly into string so 
# for that we use f-String or format method

age = 36
# txt = "i am umair , i am " +age  
# print(txt)

# soluation  F=String
# .3f mean with 3 decimal numbers
print(f"i am umair . i am {age:.3f} year old")


#Bool Function

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print("The False Values")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print("The object of my class is ")
print(bool(myobj))

## function can return Boolean
print(" returning the function")
def myFunction():
    return True

print(myFunction())

# if function return true print yes
def muFunction():
    return True
if muFunction:
    print('Yes')
else:
    print('NO')


#isinstance bool

x =200.0

print(isinstance(x,int))

