#list creation
list_   = [10, 20, 30]
print(list_)
sum=0
for i in list_:
    sum+=i
    print(type(i))
print("The sum of the list is ",sum)

# check type of list
print(type(list_))

# list can have duplicated Values,string values ,in single list we can have each type of values  
list_   = [10, 20, 10, 30,'ali','hamza']
print(list_)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)


# list construnction 
list_1 = list((10,2,3,5,3))
print(list_1)

print(type(list_1))

#accessing the list

# access the list 3rd value at index 2
print(list_1[2])

#negative index used for decending order to access list 
print(list1[-1])

# access from index a-b

print(list1[1:3])

print(list1[:3])

print(list1[1:])

print(list1)

# check if item exists in list
if "orange"in list1:
    print("yes the item exist in the list ")
else:
    print("oops! unfortunatly item is not exists in list")


## change the list items 

fruits = ["apple", "banana", "cherry","gawa"]
fruits[1]= "orange"
print(fruits)

# change multiple items

fruits[1:3] = ["mango", "watermelon"]
print("The list of fruits after ranges change")
print(fruits)


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

fruits[1:3] = ["PineApple"]

print(fruits)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#insert method used to insert the value wothout replacing any item 

fruits.insert(1, "grapes") 

print(fruits)

# append methon is used to add item at the end of the list 
print("\n\n the Append functions\n")

fruits = ['apple', 'banana', 'cherry']

fruits.append("orange")
print(fruits)

#Extend list is used to to extend the list into list
print("\n After using the Extend Function\n")
fruits.extend(list1)
print(fruits)

# we can add any iterable 
iter_ = (12,11,13,15)
fruits.extend(iter_)
print("\n after adding other iterable in list\n")
print(fruits)

## removing the lsit items
print("\n List item removing items\n")

fruits = ['apple', 'banana', 'cherry','banana']
fruits.remove("apple")
print(fruits)

# when the duplicated 
fruits.remove('banana')
print(fruits)

# remove specific index 
fruits = ['apple', 'banana', 'cherry','banana']
fruits.pop(2)
print(fruits)
# .pop removes the by default lat item of the list
fruits = ['apple', 'banana', 'cherry','banana']
fruits.pop()
print(fruits)

#del Keyword
print('\n del key word working \n')
fruits = ['apple', 'banana', 'cherry','banana']
# it is used to del a special item of the list
del fruits[0]
print(fruits)

# it can delete complete list 
del fruits

## Clear Method
print("after applying clear()")
fruits = ['apple', 'banana', 'cherry','banana']
fruits.clear()

print(fruits)


print("\n Loop through list\n")
fruits = ['apple', 'banana', 'cherry','banana']
for i in fruits:
    print(i)

## loop through index
for i in  range(len(fruits)):
    print(i)


#iteraton through while loop

i=0
while i < len(fruits):
    print(fruits[i])
    i+=1

# loop uisng list comprehension
print("\nComprehension list\n")
fruits = ['apple', 'banana', 'cherry','banana']
[print(x) for x in fruits]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)

# with comprehension list
print("list with comprehension")
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "cherry"]
print(newlist)

newlist = [x for x in fruits]
print(newlist)

# use range function to create iterable 
newlist= [x for x in range(10)]
print(newlist)

# list of number to get greater or equal to 5
newlist = [x for x in newlist if x >=5]
print(newlist)

# make values in upper case  latter in list using comprehension
newlist = [x.upper() for x in fruits ]
print(newlist)

newlist = ["hello" for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# List sorting
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
# number list 
num_list = [100, 50, 65, 82, 23]
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)

def myfunc(n):
    return abs(n- 50)
num_list = [100, 50, 65, 82, 23]
num_list.sort(key=myfunc)
print(num_list)


# case in sensetive sort
fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort(key=str.lower)
print(fruits)
fruits.reverse()
print(fruits)

# copy list 
print("\n copy list function \n")
fru = fruits.copy()
print(fru)

#list method

myFru = list(fruits)
print("list method copy ")
print(myFru)

# slice  method copy

slice_list = fruits[:]
print(slice_list)

#join list 
print("\n Join liat methods\n")
com_list = fruits + num_list
print(com_list)

# append function 
for x in num_list:
    fruits.append(x)
print(fruits)

# extend method

num_list.extend(fruits)
print(num_list)

