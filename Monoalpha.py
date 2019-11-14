import random
randomTokens = random.sample(range(0,26),26)
bond = []

def Monoalpha(plainText):
    global randomTokens, bond
    cipherText, textLen, randomChars = "", len(plainText), [chr( 65 + i ) for i in randomTokens]
    cipherText += "".join(randomChars[x] for x in range(textLen))
    bond += [ cipherText[i] + plainText[j] for i,j in zip(range(textLen), range(textLen))]
    print("Decrypted Text ",decrypt(cipherText))
    return cipherText

def decrypt(cipher):
    plainText = "".join(bond[index][1] for index in range(len(cipher)))
    return plainText
    
plainText = input("Enter the intended text : ").upper().replace(" ","")
print(Monoalpha(plainText))