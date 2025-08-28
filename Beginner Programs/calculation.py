def add(x,y):
    return x + y
    
def sum():
    return x - y
   
def multiply(x,y):
    return x * y
    
def div(x,y):
    if y == 0:
        print("ERROR ! division by Zero")
    return x / y

print("Enter following option")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

op = input("Enter option :")
x = int(input("Enter First number :"))
y = int(input("Enter Second number :"))

if op == '1' :
   print(f"Result :{x} + {y} = {add(x,y)}")
elif op == '2':
   print(f"Result :{x} - {y} = {sum(x,y)}")
elif op =='3':
   print(f"Result :{x} * {y} = {multiply(x,y)}")
elif op == '4' :
    print(f"Result :{x} / {y} = {div(x,y)}")
