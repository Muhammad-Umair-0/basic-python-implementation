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

#del keyword is used to delete the dictionary
del dic
# print(dic)  # it will raise the error because we already delete the dictionary 