import datetime
x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.strftime("%A"))


# x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# Python Math 
print("\n python min_max")
# min max

print(min(10,9,25))
print(max(10,9,25))

# absolute positive Value

x = abs(-8.25)
print(x)

# power function
x = pow(4,2)
print(x)

## Math Module
import math
#square root
print(math.sqrt(64))

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

print(math.pi)

## python json 

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])


# python to Json conversion

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# Python Regular Expression
print("\n The Reqular Expression Topic is started")
import re
txt = "The rain in Spain"
x = re.search("The.*Spain$",txt)
print(x)

x= txt.split(" ")
print(x)

# find all

x = re.findall("ai",txt)
print(x)

x = re.findall("portugal",txt)
print(x)

#search
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# split the ext at space
x = re.split("\s", txt)
print(x)
#split at just 1st escape
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# replace the white spce with 9
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Replace the 1st 2 occurance 
txt = "The rain in Spain"
x = re.sub("\s", "9", txt,2)
print(x)

# match object
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

#.spain() function
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

print(x.group())

import re
txt = 'The rain in Spain'
x = re.search('a', txt)
print(x.start())

import re
txt = 'The rain in Spain'
x = re.search('\s', txt)
print(x.start())