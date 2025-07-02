import numpy as np
from numpy import random



##genrate a number from 1st 100
x = random.randint(100)
print(x)

#genrate a random float 
x = random.rand()
print(x)

# Genrating the random 1-D array 
x = random.randint(100, size=(5))
print(x)
#Genrate random 2-D array 
x = random.randint(100, size=(3,5))
print(x)
# same but values in float 
x =random.rand(3,5)
print(x)

# chose random value from the given array 
x = random.choice([3, 5, 7, 9])
print(x)

# will make a  2-D array 
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

# DAta distribution
x = random.choice([3, 5, 7, 9], p=[0.1, 0.1, 0.1, 0.7], size=(100))
print(x)
# 2-D array with 3 rows
    
x = random.choice([3, 5, 7, 9], p=[0.1, 0.1, 0.1, 0.7], size=(3,5))
print(x)


# Data Shuffle 
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

# Permutation 

print(random.permutation(arr))



## seaborn 
## matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# plotting Displot
sns.displot([0,1,2,3,4,5])
plt.show()

# Displot without histogram
sns.displot([0,1,2,3,4,5],kind='kde')
plt.show()


##Binomial Distribution
x = random.binomial(n=10, p=0.5, size=10000)
print(x)

#visualizing the binomial distribution
sns.displot(random.binomial(n=10, p=0.5, size=10000), kde=True)
plt.show()

#bionomial and normal distribution

data  = {
    "binomial": random.binomial(n=10, p=0.5, size=10000),
    "normal": random.normal(loc=5, scale=2, size=10000)
}

sns.displot(data, kind='kde')
plt.show()

#poisson distribution
print("\nPoisson Distribution")
X = random.poisson(lam=2, size =10)
print(X)

#visualizing the poisson distribution
sns.displot(random.poisson(lam=2, size=1000), kde=True)
plt.title("Poisson Distribution")
plt.show()

# D/b/w noral and poisson distribution
data = {
    "normal": random.normal(loc=5, scale=2, size=10000),
    "poisson": random.poisson(lam=5, size=10000)
}
sns.displot(data, kind='kde')
plt.title("Normal vs Poisson Distribution") 
plt.show()

#difference between bimomial and poisson distribution
data = {
    "binomial": random.binomial(n=10, p=0.5, size=10000),
    "poisson": random.poisson(lam=5, size=10000)
}
sns.displot(data, kind='kde')
plt.title("Binomial vs Poisson Distribution")
plt.show()


# Uniform Distribution
x =random.uniform(size =(2,3))
print("\nUniform Distribution")
print(x)
# Visualizing the uniform distribution
sns.displot(random.uniform(size=1000), kde=True)
plt.title("Uniform Distribution")
plt.show()

# Logistic Distribution
x = random.logistic(loc=1,scale=2,size=(2,3))
print("\nLogistic Distribution")
print(x)

# Visualizing the logistic distribution
sns.displot(random.logistic(loc=1, scale=2,size=1000))
plt.title("Logistic Distribution")
plt.show()

#normal distribution vs logistic distribution
data = {
    "normal" : random.normal(scale=2, size=100),
    "logistic": random.logistic(size=100)
}

sns.displot(data, kind='kde')
plt.title("Normal vs Logistic Distribution")
plt.show()

#multinomial distribution
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print("\nMultinomial Distribution")
print(x)

#Chi-Squared Distribution
x = random.chisquare(df=2, size=(2,3))
print("\nChi-Squared Distribution")
print(x)


# Visualizing the Chi-Squared distribution
sns.displot(random.chisquare(df=2,size=100), kde=True)
plt.title("Chi-Squared Distribution")
plt.show()


#Rayleigh Distribution
x = random.rayleigh(scale=2, size =(2,3))
print("\nRayleigh Distribution")
print(x)    

# Visualizing the Rayleigh distribution
sns.displot(random.rayleigh(scale=2, size=1000), kde=True)      
plt.title("Rayleigh Distribution")      
plt.show()

#pareto Distribution
x =random.pareto(a =2, size=(2,3))
print("\nPareto Distribution")
print(x)

# Visualizing the Pareto distribution
sns.displot(random.pareto(a=2, size=1000))
plt.title("Pareto Distribution")
plt.show()


#zipf Distribution
x = random.zipf(a=2, size=(2,3))
print("\nZipf Distribution")
print(x)

# Visualizing the Zipf distribution
sns.displot(random.zipf(a=2, size=1000), kde=True)
plt.title("Zipf Distribution")
plt.show()
# We can also visualize the Zipf distribution using a bar plot
import matplotlib.pyplot as plt
x = random.zipf(a=2, size=1000)
plt.hist(x, bins=30, density=True)
plt.title("Zipf Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
