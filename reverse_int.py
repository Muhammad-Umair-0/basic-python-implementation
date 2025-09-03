# method:1   string slicing 
n = int(input("enter a integer value"))
n_str = str(n)

rev_n = n_str[::-1]
print(rev_n) 
print("abc",rev_n [:-2])

if n <0 :
    rev_int = int('-'+rev_n [:-1])
else:
    rev_int = int(rev_n)

print(rev_int)
    


