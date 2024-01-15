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
"""

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

my_list = ["Hello", "World", 72, True, 5.0]

print( my_list[0] ) # "Hello"
print( my_list[1] ) # "World"
print( my_list[2] ) # 72
print( my_list[3] ) # True
print( my_list[4] ) # 5.0
# In Reverse
print( my_list[-1] ) # 5.0
print( my_list[-2] ) # True
print( my_list[-3] ) # 72
print( my_list[-4] ) # "World"
print( my_list[-5] ) # "Hello"