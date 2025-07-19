def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y==0:
      return 'cannot divided by zero'
    return x/y

num1=float(input('Enter first number:'))
operator=input('Enter any operator +,-,*,/,//')
num2=float(input('Enter second number'))

if operator =='+':
    print('Result',add(num1,num2))

elif operator =='-':
    print('Result',subtract(num1,num2))

elif operator =='*':
    print('Result',multiply(num1,num2))

elif operator =='/':
    print('Result',division(num1,num2))
else:
    print('invalid input')