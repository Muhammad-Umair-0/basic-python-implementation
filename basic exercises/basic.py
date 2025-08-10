sum = 0
multi = 0
def add_multi(num1,num2):
    sum = num1 +num2
    multi = num1 * num2
    if multi >=1000:
        return multi
    else:
        return sum
    

print(add_multi(25,5))


#display current and previous number with sum
previous =0
for i in range(10):

    current = i
    print(f"previous number is {previous} the current number is {current}  sum = {previous+current}")
    previous=i

# characters present at even index
str = "MEri_malik"
n = int(len(str))
for i in range(0,n,2):
    print(f"inex {i}")
    print(str[i])

print(str[0::2])


# Ex 4 remove 1st n characters from n 
print("\n removing numbers of characters")
def remove_char(words,n):
    w_len = len(words)
    for i in range(0,w_len-1):
        if i>=n:
            print(words[i])

print(remove_char("MEri_tech",3))
print(remove_char("MEri_tech",2))

#EX 5 compare the 1st and last element of the list or index
print("compare the indexes are same or not")
numbers_x = [10, 20, 30, 40, 10]

numbers_y = [75, 65, 35, 75, 30]

a = numbers_x[0] == numbers_x[-1]
print(a)

b = numbers_y[0]==numbers_y[-1]
print(b)
    