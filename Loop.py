# while loop
i= 1
while i<6:
    print(i)
    i +=1

#exit the loop while i=3
i=1
while i<6:
    print(i)
    if i==3:
        break
    i +=1

#continue statement 

i=1
while i<6:
    i +=1
    if i==3:
        continue
    print(i)


## For Loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# break in loop 

for x in fruits:
    print(x)
    if x== 'banana':
        break

print("print after break")
for x in fruits:
    print(x)
    if x== 'banana':
        break

    print(x)



# range funtion 

for i in range(2,7,2):
   if i==4: break
   print(i) 
else:
    print("Finally finihed")



#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
