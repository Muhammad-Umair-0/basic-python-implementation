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

