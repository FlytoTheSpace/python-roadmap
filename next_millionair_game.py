content = [
    {
        'question': "What's the GOD's programming Lanuage?",
        'choices': [
            'Python',
            'JavaScript',
            'Java',
            'C'
        ],
        'answer': 4,
        'prize': 1000
    },
    {
        'question': "Minecraft PC version is built with?",
        'choices': [
            'JavaScript',
            'Python',
            'Java',
            'C++'
        ],
        'answer': 3,
        'prize': 5000
    },
    {
        'question': "Which Language is used in Web Browsers",
        'choices': [
            'Web Assembly',
            'JavaScript',
            'PHP',
            'Python'
        ],
        'answer': 2,
        'prize': 10000
    },
    {
        'question': "When was windows 7 Released",
        'choices': [
            '2006',
            '2008',
            '2007',
            '2009'
        ],
        'answer': 2,
        'prize': 12000
    }
]
prize = 0
abcToNum = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for level in content:
    print('\n', level['question'], '\n')
    print(f"A: {level['choices'][0]}        B: {level['choices'][1]}")
    print(f"C: {level['choices'][2]}        D: {level['choices'][3]}", '\n')
    
    choice = input('Pick A/B/C/D > ').lower()
    
    if (choice != 'a' and choice != 'b' and choice != 'c' and choice != 'd' and choice != 'exit'):
    
        print('Invalid Choice')
        break
    
    elif(level['answer'] == abcToNum[choice]) :
    
        prize = level['prize']
        print(f"Your Current Prize Money is Now ${prize}")
        
    elif (choice == 'exit'):
        break
    
    else:
        print("Incorrect answer")
        break
    
print(f"You're returning Home with ${prize}")