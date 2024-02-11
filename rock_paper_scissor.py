import random

options = ['rock', 'paper', 'scissor']

optionToNum = {
    'rock': 0,
    'paper': 1,
    'scissor': 2 
}

def printResult (user, computer):
    print("You      Computer")
    print(f"{user.capitalize()}      {computer.capitalize()}")
    print('\n')

print("Enter `exit` to Quit")

while True:
    userInput = input("Rock/Paper/Scissor > ").lower()
    
    if userInput != 'rock' and userInput != 'paper' and userInput != 'scissor' and userInput != 'exit':
        print("Invalid Input")
        break
    elif userInput == 'exit':
        print("Exiting...")
        break
    computerInput = random.choice(options)
    
    userInputNum = optionToNum[userInput]
    computerInputNum = optionToNum[computerInput]
    
    if userInputNum == computerInputNum:
        
        print("\nIt's a Draw!\n")
        printResult(userInput, computerInput)
        
    elif (userInputNum == 0 and computerInputNum == 1) or (userInputNum == 1 and computerInputNum == 2) or (userInputNum == 2 and computerInputNum == 0):
        
        print("\nYou've Lost!\n")
        printResult(userInput, computerInput)

    else:
        print("\nYou've Won\n")
        printResult(userInput, computerInput)
