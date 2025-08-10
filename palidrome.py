# Python Programs to Check Palindrome Number
# method 1: string slicing 
n = 12321
n_str = str(n)
rev_n_str = n_str[::-1]

if n_str ==rev_n_str:
    print(f"{n} is a palindrome")




