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


