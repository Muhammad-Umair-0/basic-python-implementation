import numpy as np


speed = [86,87,88,86,87,85,86]

x = np.std(speed)

print(x)

# Variance
# -->1  find mean 
sum =0
n =0
for i in(speed):
    sum += i
    n +=1
print(sum)
print(n)
avg = sum/n
print(avg)


#--> find th edifference from mean
diff = []
for i in speed:
    diff.append(i-avg)


print(diff)

# 3--> find the square value
diff_sqr = []
for i in diff:
    diff_sqr.append(i**2)

print(diff_sqr)

diff_sqr_sum = 0
for i in diff_sqr:
    diff_sqr_sum +=i

print("\n The variance is ")
print(diff_sqr_sum/n)

# calculate the variance using numpy

x = np.var(speed)
print("\n The variance using the numpy", x)


# percentile 

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.percentile(ages, 90)

print("\n The percentile is\t",x)

