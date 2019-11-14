from collections import OrderedDict

def playfair(plainText,key):

    cipherText = ""
    plainText += "X" if len(plainText)%2 !=0 else ""
    tempKS   = list(key) + [chr(65+init) for init in range(0,26) if chr(65+init) != 'J']
    keySquare = list(OrderedDict.fromkeys(tempKS))
    
    for i in range(0,len(plainText),2):

        index1, index2 = keySquare.index(plainText[i]), keySquare.index(plainText[i+1])

        if index1 % 5 == index2 % 5:

            cipherText += keySquare[(index1+5)%25] + keySquare[(index2+5)%25]

        elif index1 // 5 == index2 // 5:

            tempInd1 = 5 * (index1 // 5) if (index1+1) // 5 > (index1) // 5 else index1 + 1
            tempInd2 = 5 * (index2 // 5) if (index2+1) // 5 > (index2) // 5 else index2 + 1        
            cipherText += keySquare[(tempInd1)] + keySquare[(tempInd2)]

        else:
            mod1, mod2 = index1 % 5, index2 % 5
            mappedIndex1, mappedIndex2 = index1 if (mod1) > (mod2) else index2, index2 if (mod2) < (mod1) else index1
            amInd1, amInd2 = mappedIndex2 + abs(mod1-mod2), mappedIndex1 - abs(mod1-mod2)
            cipherText += (keySquare[amInd1] + keySquare[amInd2]) if mappedIndex2 == index1  else (keySquare[amInd2] + keySquare[amInd1])

    return cipherText

plainText = input("Enter the plain text : ").replace(" ","").upper()
key = input("Enter the key : ").replace(" ","").upper()
print(playfair(plainText,"".join(OrderedDict.fromkeys(key))))

