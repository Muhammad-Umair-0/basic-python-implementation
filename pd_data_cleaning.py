import pandas as pd
import matplotlib.pyplot as plt

# read data
df = pd.read_csv("data.csv")
print(df.head(5))
# get null values 
null_values = df.isnull().sum()
print(null_values)
#dropping the null Values
df.dropna(inplace=True)
print("The data frame is")
print(df.duplicated())


df.drop_duplicates(inplace=True)
print(df)

# Correlation b\w the data sets
print(df.corr())


#plotting 
df.plot()
plt.show()

#scatter plot
df.plot(kind="scatter", x='Duration', y='Calories')
plt.title("Duration vs Calories")
plt.show()

df.plot(kind="scatter", x='Duration', y='Maxpulse')
plt.title("Duration vs Maxpulse")
plt.show()