import pandas as pd
# read data
df = pd.read_csv("data.csv")
print(df.head(5))
# get null values 
null_values = df.isnull().sum()
print(null_values)
#dropping the null Values
df  =df.dropna(inplace=True)
print(df)