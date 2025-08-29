#Factorial program
n = 6

fact = 1
for i in range (1 , n +1):
    fact *= i
print(fact)

#Factorial program useing recursion function

def fact(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(n))
