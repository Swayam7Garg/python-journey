# hello world
# print("hello world")
# variables - used to store data
name = "Swayam"
roll_number = 23
percentage =78.5
isstudent = True
print(name , roll_number , percentage , isstudent)
print(type(name))
print("my name is" + name)#No auto space(only for same datatype concatenation)
print("My Name is",name)#auto space


#print expressions
print("My percentage has changed to " , percentage -1.0)

#print with sperator
print(name , roll_number , percentage , isstudent , sep=",")
char = "a"
print(ord(char))

acii = 98
print(chr(acii))

print(chr(100))


# to take any input
name = input("enter the name :")
print(name)# always take as the string datatype so do typecasting

age = int(input("enter the age :"))
print(age)