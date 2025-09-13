# Reverse a string 

a = "hello"
print(a[::-1])


# Check if a string is a palindrome

def is_palindrome_String(s):
   
    return s == s[::-1]

is_palindrome_String("madam")


# Check if a number is a palindrome
def is_palindrome_number(n):

    if str(n) == str(n)[::-1] :
        print("it is Palindrome Number", n)
    else:
        print("it is Not a Palindrome Number", n)
 
is_palindrome_number(121)


# Find the largest of three numbers
def largest_of_three(x, y, z):
    if (x >= y) and (x >= z):
        largest = x
    elif (y >= x) and (y >= z):
        largest = y
    else:
        largest = z
    return largest

print(largest_of_three(10, 20, 15))


# Factorial of a number
def factorial(g):
    if g == 0 or g == 1:
        return 1
    else:
        return g * factorial(g - 1)

print(factorial(5))  # Output: 120


# factorial using recursion & loop)
def factorial(l):
    return 1 if l == 0 else l * factorial(l -1)

print(factorial(5))


#fivonacci series
def fibonacci(d):
    d,f = 0,1
    for _ in range(d):
        print(d ,end=" ")
        d,f = d, d+f

fibonacci(10)
