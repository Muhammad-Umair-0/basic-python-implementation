import numpy as np


# creating first array 
# converting a list to an array 

arr = np.array([1,2,3,4])
print(arr)
print(type(arr))

# converting a tuple to an array 

arr = np.array((4,5,7,8,9,0))
print(arr)
print(type(arr))

# 0-D array
a = np.array((42))
print(a)

# 1-D array 
b = np.array([1,2,3,4,5,6,7])
print(b)

# 2-D array  

c = np.array([[1,2,3], [4,5,6]])
print(c)

# 3-D array 

d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(d)

# test 
print("\n")
e = np.array([[[1, 2, 3], [4, 5, 6], [1, 2, 3]]])
print(e)
## check numbers of dimensions
print("The numbers of Dimensions are")
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# creating an array with the number of dimensions 
arr = np.array([1,2,3,4,5],ndmin=5)
print(arr)
print("Numbers of dimension are ", arr.ndim)



## Accessing Array Element
print("\n Accessing array Element\n")
arr = np.array([1,2,3,4,5])
print(arr[3])

# adding the Element of array
print(arr[2] + arr[3])

#accessing the 2D array
# accessing 1 row and 2nd column

arr = np.array([[1,2,3,4,5], [6,7,8,9,0]])
print(arr)
print("2nd element on 1st row:", arr[0,1])

# Access 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0,1,2])

# Negative indexing

arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print("last Element from the 2nd dim:  ",arr[1,-1])


## array Slicing 
print("\n Array slicing \n")
arr = np.array([1, 2, 3, 4, 5, 6, 7,7])
print(arr[1:5])
# slince from idex 4 to end
print(arr[4:])
##from 0 to 4(not included)
print(arr[:4])
#negative slicing 
print(arr[-3:-1])
#steps  to slice the value 
print(arr[1:5:2])
# return the entire element with steps 
print(arr[::2])


##slicing through 2d array 
print("\n slicing through 2D array")
arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])
#from both elemnts return index 2
print(arr[0:2, 2])
#from both elements slice from index 1 to 4 (4 not included)
print(arr[0:2,1:4])


# Numpy Datatypes
print("\n Cecking the data types of numpy array")
arr = np.array([1,2,3,4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# define data types while creating an array

arr = np.array([1,2,4,5,6], dtype="S")
print(arr,arr.dtype)

#create array with 4 byte integer
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

#converting a dtype on existing array
# note : if value cannot be converted it will raise an error
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

#from integer to boolein
arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)


##Copy and View
print("\n copy vs View")
#Copy

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 11
print(arr)
print(x)

#view
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 11
print(arr)
print(x)

# check if array own its data
arr = np.array([1,2,3,4,5])
x= arr.copy()
y= arr.view()

print(x.base)
print(y.base)



#shape of Array
print("\n array shape")
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

#array with dimensions 
arr  = np.array([1,2,3,4,5],ndmin=5)
print(arr)
print(arr.shape)


#Reshape array 
print("\n Reshape the Array\n")
#converting from 1 dim to 2-D

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newa = arr.reshape(3,4)
print(newa)
D3 = arr.reshape(2,3,2) 
print(D3)

#chech if return array is a copy or view
print(newa.base)
#convert 1D array to 3d array 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

# flattening the array 
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)


## Iterating Array 
# 1-D array 
arr = np.array([1,2,3])

for x in arr:
    print(x)


# 2-D array 
arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in arr:
    print(x)
#iterate Each scalor element of 2-D array 
for x in arr:
    for y in x:
        print(y)


#iteration through the 3d arry
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)


#nditer
print("\n nditer")
for x in np.nditer(arr):
    print(x)

arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

#skipping the 1 element 

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)


# ndenumerate
arr = np.array([[1, 2, 3],[4,5,6]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
