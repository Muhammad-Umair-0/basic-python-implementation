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