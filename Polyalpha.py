def polyalpha(plainText):
    print("PlainText : ",plainText)
    plainText, mappedSet, reckonedVal, tempList = plainText.upper(), [], ord('A'), []
    
    for i in range(0,26):
        for j in range(0,26):
            if reckonedVal > 90:
                reckonedVal = 64 + ((reckonedVal - 90) % 26)
            tempList.append(chr(reckonedVal))
            reckonedVal += 1
        mappedSet.append(tempList)       
        tempList = []
        reckonedVal += 1

    setPtr, cipherText = 0, ""
    
    for i in range(0,len(plainText)):
        index = ord(plainText[i]) - 65
        if index < 0:
            cipherText += " "
            continue
        cipherText += mappedSet[setPtr][index]
        setPtr += 1
    return print("CipherText : ",cipherText)


enteredText = input("Enter the intended text : ")

polyalpha(enteredText)