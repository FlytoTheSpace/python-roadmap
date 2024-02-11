import random

msg = "Hello, World"

def encrypt (message):
    arrMsg = [];

    base64 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '=', '/', '+']

    for i in range(len(message)):
        arrMsg.append(message[i])
    arrMsg.append(base64[random.sample(range(0, 26), 1)[0]])
    arrMsg.append(base64[random.sample(range(0, 26), 1)[0]])
    arrMsg.append(base64[random.sample(range(0, 26), 1)[0]])
    arrMsg.insert(int(len(arrMsg)/2), base64[random.sample(range(0, 26), 1)[0]])
    arrMsg.insert(int(len(arrMsg)/2), base64[random.sample(range(0, 26), 1)[0]])
    arrMsg.insert(int(len(arrMsg)/2), base64[random.sample(range(0, 26), 1)[0]])
    arrMsg.insert(0, base64[random.sample(range(0, 26), 1)[0]])
    arrMsg.insert(0, base64[random.sample(range(0, 26), 1)[0]])
    arrMsg.insert(0, base64[random.sample(range(0, 26), 1)[0]])

    arrMsg.reverse()

    encMsg = ''

    for i in arrMsg:
        encMsg += i

    return encMsg

def decrypt (message):
    
    arrMsg = []

    base64 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '=', '/', '+']

    for i in range(len(message)):
        arrMsg.append(message[i])
    
    arrMsg.reverse()
    
    arrMsg.pop(0)
    arrMsg.pop(0)
    arrMsg.pop(0)
    
    arrMsg.pop(int(len(arrMsg)/2))
    arrMsg.pop(int(len(arrMsg)/2))
    arrMsg.pop(int(len(arrMsg)/2))
    
    arrMsg.pop()
    arrMsg.pop()
    arrMsg.pop()
    decMsg = ''
    for i in arrMsg:
        decMsg += i

    return decMsg

ciphertext = encrypt("Password:1234")

print(ciphertext)
print(decrypt(ciphertext))
