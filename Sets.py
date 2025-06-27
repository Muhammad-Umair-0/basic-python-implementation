# creation of set
# duplicate values will be ignored

set1 = {1,2,4,5,6,4, False,0,1,True}
print(set1)
# in sets True,1 count as same value 
# and False ,0 will be the same value 

# sets item and data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False,99}

print(set1,"\n",set2,"\n",set3)

# set can contain  values of differnct types
set1 = {1,2,4,5,6,4, False,0,1,True, "ali",'hamza'} 
print(set1)
print(type(set1))

## set construction 
set_   = set((2,4,6,7,8,0))
print(set_)

# we cannot access the items using index but we can access using loop
for x in set1:
    print(x)


# we can check if item present in the set
print("bnana" not in set1)

## add item 
# add() method
set1.add("meri")
print(set1)

#to add the item of two different sets

set3.update(set2)
print(set3)

# add any iterable 
set1 = {1,2,3,4,4}
list1 = ['a','b']
set1.update(list1)
print(set1)