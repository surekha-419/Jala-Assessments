#Write a function for arithmetic operators(+,-,*,/) 

a = 25
b = 45
opr = input("Enter the operator (+,-,*,/)")
if opr =='+':
    print(a+b)
elif opr =='-':
    print(a-b)
elif opr =='*':
    print(a*b)
elif opr =='/':
    print(a/b)
else:
    print('wrong input program terminated ')


#Write a method for increment and decrement operators(++, --) 
x = 10
x += 1
x -= 4 
print("After increments:", x)
print("After Decrement by 4:", x)

#Write a program to find the two numbers equal or not.

Num1= 25
Num2= 45

if Num1 == Num2:
    print("Equal")
else:
    print("Not Equal")

# Program for relational operators (<,<==, >, >==) 

a = 25
b = 45
print("a < b :", a < b)
print("a <= b:", a <= b)
print("a > b :", a > b)
print("a >= b:", a >= b)

#Print the smaller and larger number 

a = 25
b = 45

if a > b:
    print("Larger:", a)
    print("Smaller:", b)
else:
    print("Larger:", b)
    print("Smaller:", a)