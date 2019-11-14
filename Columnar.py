import math

def columnar(plainText, key):

    keySize, pTSize, sortedKey, cipherText, columns, iniEl = len(key), len(plainText), sorted(key), "", [], 0

    probRows = math.ceil(pTSize/keySize)
    elements = probRows * keySize

    if pTSize != elements : plainText += ["X" for rem in range(elements - pTSize)]

    while iniEl < keySize: 
        interCols, xEl = [], iniEl
        while xEl <= elements-1:
            interCols.append(plainText[xEl]) 
            xEl += keySize
        columns.append(interCols)
        iniEl += 1

    for token in sortedKey:

        cipherText += "".join(str(x) for x in columns[key.index(token)])
        del columns[key.index(token)]
        key.remove(token)

    return cipherText

plainText = input("Enter the plain text : ").replace(" ","").upper()
key = input("Enter the key : ").replace(" ","").upper()
print(columnar(list(plainText),list(key)))
