def Hill(plainTextBlock, keyMatrix, mode):

    value, genText = 0, ""

    for i in range(mode):

        for j in range(mode): value += ( ord( keyMatrix[i][j] ) - 65 ) * ( ord( plainTextBlock[j] ) - 65 )

        genText += chr( 65 + ( value % 26 ) )   
        value = 0

    return genText

def HillSplit(plainText, key, mode):

    plainText, key, textLen, keyLen = plainText.upper(), key.upper(), len(plainText), len(key)
    keyValues = [ (ord(key[i])-65)  for i in range(len(key)) ]
    textSplit, cipher, x, token = [], "", 0, 3 if mode == "T" else 2 

    if textLen % token != 0:  plainText += "".join( "K" for i in range( token - textLen % token ))

    if keyLen < pow(token,2): key += "".join( chr(65+i) for i in range( pow(token,2) - keyLen )) 
    else : key = "".join( key[char] for char in range( pow(token,2) ) )

    keySplit = [ key[i:i+token] for i in range(0,len(key),token)]
    textSplit += [ plainText[x:x+token]  for x in range(0, len(plainText), token) ]
    cipher += "".join( Hill( textSplit[i], keySplit, token ) for i in range(len(textSplit)))
    
    return cipher
    
pT = input("Enter plain text for encryption : ").replace(" ","")
mode = input("Press D for digraph \nPress T for trigraph : ___")
key = input("Enter the key : ").replace(" ","")
print(HillSplit(pT,key, mode))