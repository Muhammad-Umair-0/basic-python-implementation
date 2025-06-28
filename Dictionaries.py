# dictionary creation 
dic = {
    "brand": "ford",
    "model":  "Mustang",
    "year":  2004
}

print(dic)

## get access by key
print(dic["brand"])
print(dic.keys())

print("The values")
print(dic.values())

#duplicate values overwrite existing values
dic = {
    "brand": "ford",
    "model":  "Mustang",
    "year":  2004,
    "year": 2000

    }
print(dic)

# Dictionary Length
print(len(dic))

# values in dictionary can be any data type
dic = {
    "brand": "ford",
    "model":  "Mustang",
    "year":  2004,
    "year": 2000,
    "color": ["red","green","blue"],
    "electric": False
 }

print(dic["color"])
print(type(dic))

# The dict() constructor
dic  = dict(name="umair", age=24, country="Pakistan")
print(dic)

# get values using Key
print(dic.get("name"))


# get keys 

x= dic.keys()
print(x) 
#any values change in dictionary effect in keys list
dic["gender"] = "Male"
print(x)

#values access
x = dic.values()
print(x)
# any change in dictionary effect the values list
dic["age"] = 25
print(x)

# get items
x= dic.items()
print(x)
#changes in dictionary make the changes in the dictionary
dic["age"] = 23
print(x)

# check if key Exist
if "name" in dic:
    print("yes! name is one of the key that exist in dictionary")

#change dictionary items 
dic["name"] = "hamza"
print(dic)

dic.update({"name": "umair"})
print(dic)


## removing items 
dic.pop("gender")
print(dic)

dic.popitem()
print(dic)
#clear method is used to clear the dictionary
dic.clear()
print("the dictionary after clear method,", dic)
#del keyword is used to delete the dictionary
del dic
# print(dic)  # it will raise the error because we already delete the dictionary 

# Loop in dictionaries

dic = {
    "brand": "ford",
    "model":  "Mustang",
    "year":  2004,
    "year": 2000,
    "color": ["red","green","blue"],
    "electric": False
 }
print("\nloop to print dictionary Values\n")
for x in dic.values():
    print(x)

print("\nloop to print dictionary keys\n")
for x in dic.keys():
    print(x)

print("\nloop to print dictionary items\n")
for x,y in dic.items():
    print(x,y)


## make a copy of dictionary 
mydic = dic.copy()
print(mydic)


mydic1 = dict(dic)
print(mydic1)



## Nested Dictionary 
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])


# Loop Through the keys and Dictionaries
for x, obj in myfamily.items():
    print(x)


    for y in obj:
        print(y + ':',obj[y])



