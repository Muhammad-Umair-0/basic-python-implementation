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

