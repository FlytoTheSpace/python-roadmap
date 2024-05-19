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
# import re
# from functools import reduce


# matchs = re.findall(".", "Hello, World!\n 64")
# print(matchs) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!', ' ', '6', '4']

# matchs = re.findall("\w", "Hello, World!\n 64")
# print(matchs) # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd', '6', '4']

# matchs = re.findall("\d", "Hello, World!\n 64")
# print(matchs) # ['6', '4']

# matchs = re.findall("\s", "Hello, World!\n 64")
# print(matchs) # [' ', '\n', ' ']


# matchs = re.findall("\W", "Hello, World!\n 64")
# print(matchs) # [',', ' ', '!', '\n', ' ']

# matchs = re.findall("\D", "Hello, World!\n 64")
# print(matchs) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!', '\n', ' ']

# matchs = re.findall("\S", "Hello, World!\n 64")
# print(matchs) # [' ', '\n', ' ']


# import asyncio
# import time

# async def function1():
#     await asyncio.sleep(6)
#     print("Done! function 1")
# async def function2():
#     await asyncio.sleep(3)
#     print("Done! function 2")
# async def function3():
#     await asyncio.sleep(4)
#     print("Done! function 3")

# async def main():
#     await asyncio.gather(function1(), function2(), function3())

# start = time.time()
# asyncio.run(main())
# end = time.time()
# print("[Async] All Done in", end-start)

# def function1():
#     time.sleep(6)
#     print("Done! function 1")
# def function2():
#     time.sleep(3)
#     print("Done! function 2")
# def function3():
#     time.sleep(4)
#     print("Done! function 3")

# def main():
#     function1()
#     function2()
#     function3()

# start = time.time()
# main()
# end = time.time()

# print("[Sync] All Done in", end-start)

import multiprocessing.process
import threading

# thread1 = threading.Thread(target=function1,args=[])
# thread2 = threading.Thread(target=function2,args=[])
# thread3 = threading.Thread(target=function3,args=[])
# start = time.time()
# thread1.start()
# thread2.start()
# thread3.start()
# print(thread1.join())
# print(thread2.join())
# print(thread3.join())

# end = time.time()
# print("Main Completed in", end-start,"seconds")

# importing modules
# from concurrent.futures import ThreadPoolExecutor
# import time

# # Functions to be executed in seperate threads

# def isEven(n, msg):
#     print(msg)
#     return True if n%2==0 else False

# numbersTobeChecked = [1, 6, 4, 5, 9]
# messages = ['W', 'o', 'r', 'l', 'd']
# max_threads = 5 # set the max amount of thread it can use

# with ThreadPoolExecutor(max_workers=max_threads) as executor:
#     results = executor.map(isEven, numbersTobeChecked, messages)
    
#     results = list(results)

#     for i in range(len(results)):
#         print(numbersTobeChecked[i], "is even?", results[i])

# Console:
# 1 is even? False
# 6 is even? True 
# 4 is even? True 
# 5 is even? False
# 9 is even? False

import multiprocessing
import time

def function1(n):
    time.sleep(n)
    print(f"Slept for {n} seconds!")
    return "Slept for {n} seconds!"

sleeplist = [5,2,3,7]

processes = []
if __name__ == "__main__":
    for i in sleeplist:
        process = multiprocessing.Process(target=function1, args=[i])
        process.start()
        processes.append(process)


for process in processes:
    process.join()
