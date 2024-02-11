"""
print("Hello World")
a = "hi!"

#Comments

print(15//3)

InputStr = input("Calculate >")
OutputStr = eval(InputStr);
print(OutputStr)

userInput = input('Pick a Number between 1-10 >')
print("Your Number is ", userInput)

age = 20

criteria = "adult" if (age>=20) else "kid";
print(criteria) # Prints: `adult`

if (age>=20):
    print("Great You're an adult");
elif (age<20):
    print("lol you're just a kid");
else:
    print("error");

# import time
# # print(time.strftime('%H:%M:%S'))
# print(time.strftime())

# if(int( time.strftime('%H')) >= 4 and int(time.strftime('%H')) < 9 ):
#     print('Good Morning!')
# elif(int( time.strftime('%H')) >= 9 and int(time.strftime('%H')) < 15 ):
#     print('Good AfterNoon!')
# elif(int( time.strftime('%H')) >= 15 and int(time.strftime('%H')) < 19 ):
#     print('Good Evening!')
# elif(int( time.strftime('%H')) >= 20 and int(time.strftime('%H')) <= 23 ):
#     print('Good Night!')
# number = 5


# match number:
#     case 0 if number < 100:
#         print("Your Number is less than a Hundred")
#     case 5:
#         print("5")


# def make_sandwitch(**ingredient):
#     print('tomato? :', ingredient['tomato'])
#     print('cabbage? :', ingredient['cabbage'])
#     print('olives? :', ingredient['olives'])
#     print('sauce? :', ingredient['sauce'])

# make_sandwitch(tomato=True, cabbage=True, olives=True, sauce="Mayonese")


# my_tuple = (1,5,4)

# my_list = list(my_tuple)

# # Modifications:
# my_list[1] = 3
# my_list.insert(1, 2)
# my_list.append(5)

# my_tuple = tuple(my_list)
# print(my_tuple)

Introduction = "Hi, my name's {} and I'm {}"

print(Introduction.format("James", 27))
# "Hi, my name's James and I'm 27"

# You define order of Insertion in The String (Index):

Introduction = "Hi, my name's {1} and I'm {0}"
			
print(Introduction.format(27, "James")) # Order of Insertion has changed
# "Hi, my name's James and I'm 27"


f"this is a set of curly brackets inside f-string: {{}} "

"""
def factorial(n):
    if(1==n or 0==n):
        return 1
    else:
        return n*factorial(n-1)

# print(factorial(5))

# def myFunction(a, b):
	# if(a<b):
		# print(a)
		# myFunction(a+1, b)
	# else:
		# print("exit!")
    # 
# 
# myFunction(4,12)

# class Person:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age

# class Student (Person): # Inherit from Person
#     def  __init__ (self, name, age, ID):
        
#         super().__init__(name, age) # Calling The Constructor of the Parent Class
        
#         self.studentid = ID

# student = Student("James", 19, 20210563597)

# print(student.name) # James
# print(student.age) # 19
# print(student.studentid) # 20210563597


# import argparse

# # Create parser object
# parser = argparse.ArgumentParser(description="Introduction") # Create a Method for adding Arguments

# parser.add_argument('name', help="Name of The User") # Argument
# parser.add_argument('--msg', '-m', default="Hello", help="Name of The User") # A Flag for special Arguments

# args = parser.parse_args() # Get all The Arguments

# print(f"{args.msg}, My name's {args.name}!")
