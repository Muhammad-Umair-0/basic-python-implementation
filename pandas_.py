import pandas as pd

mydata = {
    "cars":['BMW', 'Volvo', 'Ford'],
    "passings": [3, 7, 2],
}

df = pd.DataFrame(mydata)
print(df)

#checaking pandas version
print("Pandas version:", pd.__version__)

# pandas series
s = pd.Series([1, 2, 3,2, 4, 5])
print("Pandas Series:")
print(s)

# If no specifice label is given, the index will be the default integer index.
print(s[2])

# create labels 
a = [1, 2, 3,2, 4, 5]
myvar = pd.Series(a, index=['a','b','c','d','e','f'])
print(myvar)

print(myvar['c'])  # Accessing by label

#  key value object as Series


cal = {
    'day1':420,
    'day2': 380,
    'day3':390
       }
df = pd.Series(cal)
print(df)

# create a series using data from day 1 to day2
df = pd.Series(cal, index=['day1','day2'])
print(df)

# DataFrames
print("\n Data Frames")
data = {
    'calories': [240,420,320],
    'duration': [50,40,45]

}

df = pd.DataFrame(data)
print(df)

# refer the row index 
print(df.loc[0])

#use list of index
# return row 0,1,2 
print(df.loc[[0,1,2]])

# add list of names given to each row 
df = pd.DataFrame(data, index = ["day1", "day2","day3"])
print(df)


#  Locate by index name
print(df.loc["day2"])


## Reading csv file
df = pd.read_csv('data.csv')
print(df.to_string)
print(df)

#check number of max rows return
print(pd.options.display.max_rows)


#reading the Json 

df1 = pd.read_json("data.json")
print("The Json data")

print(df1)


# data analysis 
print("\n Data analysis")
print(df1.head())
# Data info 
print("data info is ")
print(df1.info())
