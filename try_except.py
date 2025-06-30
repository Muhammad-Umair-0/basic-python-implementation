# Try to load x,  x is not define so it run except block

try:
    print(x)
except:
    print("An exception error occur")


# many Exceptions

try:
    print(x)
except NameError :
    print("variable x is not define")
except:
    print("something else went wrong")

#Else
try:
    print("Hello word")
except:
    print("something went wrong")
else:
    print("Nothing went wrong")

#Finally
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("The 'try except' is finished")


# to open and write the to a file that is not writeable
try:
    f = open("demofile.txt")
    try:
        f.write("lorum ipsunm")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong opening the file")

# raise keyword

# x = -1
# if x<0:
#     raise Exception("Sorry no number below zero")

#raise type error
x = "hello"
if not type(x) is int:
    raise TypeError("only integer are allowed")