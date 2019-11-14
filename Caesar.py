def Caesar(plainText):
    ordeal = [ ord(plainText[i]) for i in range(len(plainText))]
    for i in range(len(ordeal)): print(ordeal[i])
    cipherText = "".join( chr( 65 + (ordeal[i]-65+3) % 26 ) for i in range(len(ordeal)))
    print(" Decipher Text ",decrypt(cipherText))
    return cipherText

def decrypt(cipher):
    sniper = [ ord(cipher[i]) for i in range(len(cipher))]
    plainText = "".join( chr(sniper[i]-3 if sniper[i]-3 > 64 else sniper[i]-3+26) for i in range(len(sniper)))
    return plainText
    
plainText = input("Enter the text for encryption : ").upper().replace(" ","")
print(Caesar(plainText))