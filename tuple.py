#touple creation
mytouple = ("Grapes","apple", "banana", "cherry")
print(mytouple)

#touple duplicates

dup_touple = ("apple", "banana", "cherry", "apple", "cherry")
print(dup_touple)

#length of touple
print("The length of my touple is",len(mytouple))
#touple with single item, we must add comma if we are making a touple of single item

touple1 = ("apple",)
print(touple1, type(touple1))

# data type 
#touple can be of any data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = (3,'5',7.3, True)
print(tuple1,tuple2,tuple3,tuple4)


### Touple Constructor

tuple_ = tuple(("apple",33,"banana"))
print(type(tuple_))


# access the touples
print(tuple_[1])
#-ve index 

print(tuple_[-1])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

print(thistuple[:4])

print(thistuple[2:])

# range of -ve index

print(thistuple[-4:-1])

# check if the value is exist in tuple

if "apple" in thistuple:
    print("Yes! Apple is in the Fruits")


# since touple are unmutable if you want to change its value you can convert it into list and then change 
# and convert back into tuple

x  = (2,3,4,5,6)
y = list(x)
y[1] = 9
x = tuple(y)
print(x)

## add tuple to tuple 

thistuple = ("apple", "banana", "cherry")
y = ("orange",)

thistuple +=y
print(thistuple)

# delete toouple
del thistuple

# print(thistuple)  #this will raise error because this touple was deleted



# unpacking of touples
fruits = ("apple", "banana", "cherry")
(green, yellow,red ) = fruits

print(green)
print(yellow)
print(red)

# using aestric

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red,blue) = fruits
print("\n using aesteric\n")
print(green)
print(yellow)
print(red)


(green, *yellow, red) = fruits
print("\n using aesteric\n")
print(green)
print(yellow)
print(red)
print(blue)

# Loop in tuple
for x in fruits:
    print(x)

# print index number in loop
for i in range(len(fruits)):
    print(i,fruits[i])


# while loop
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
i=0
while i<len(fruits):
    print(fruits[i])
    i+=1

# Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#tuple multiplicationa
multi_tup = fruits*2
print(multi_tup)
print(tuple2*2)

#count metho
print(fruits)
print(fruits.count("cherry"))