#Write a program to print your name. 
print("Surekha")


#in single line comment it displays #
"""multi-line shows like this"""


#Define variables for different Data Types int, Boolean, char, float, double and print on the Console. 
a= 25
b= 3.7
c= "hi"
is_student=True
print("integer value:",a)
print("float_value:",b)
print("string value:",c)
print("boolean value:",is_student)


#Define the local and Global variables with the same name and print both variables and understand the scope of the variables 
name="SuSha"

def show():
    name="SuHa"  # local
    print("Inside:", name)

show()
print("Outside:", name) #global