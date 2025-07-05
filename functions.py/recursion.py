def factorial(n):
    if (n==1) or (n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number: "))
print(f"Factorial of number is {n} : {factorial(n)}")    




"""
5 = 5 * 4 * 3 * 2 * 1
4 = 4 x 3 x 2 x 1
5 = 5 * (n-1)!
"""