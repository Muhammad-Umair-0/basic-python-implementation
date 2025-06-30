# to read the file
f= open("demo.txt")
print(f.read())

#using with statement 
with open("demo.txt") as f:
    print(f.read())


# code to closed the file
f = open("demo.txt")
print(f.readline())
f.close()

# read only part of the file

with open("demo.txt")as f:
    print(f.read(5))

# readline
with open('demo.txt') as f :
    print(f.readline())
    print(f.readline())


# by looping the line you can readthe file line by line
print("after the loop\n")
with open("demo.txt") as f:
    for x in f:
        print(x)


# now we append more text in the file
with open('demo.txt', 'a') as f:
    f.write("Now file has more content!")


#read the file after appending more text
with open('demo.txt') as f:
    print(f.read())


# overwrite the entire file
with open("demo.txt", "w") as f :
    f.write("woops!  i have deleted the content !")


#open and read the file afyer over writing
with open('demo.txt') as f:
    print(f.read())


# remove file

import os
os.remove('demo.txt')


