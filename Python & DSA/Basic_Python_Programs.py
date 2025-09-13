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



