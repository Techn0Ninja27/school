def stringCutter(string):
    '''cuts string to 3 characters long'''
    if len(string) <= 3: #check length of sting
        return string
    else:
        return string[0:3] #return first 3 characters


string = "less goo!" #dababy
print(stringCutter(string))

def stringUpper(string):
    '''if 2 of first 4 characters are uppercase, return entire string uppercase'''
    firstChars = [] #opens list
    for i in range(0,4):
        firstChars.append(string[i]) #appends first 4 characters to list
    amountUppercase = 0 #how many characters are uppercase
    for i in range(0,4): #loop to save code
        if firstChars[i].isupper(): #checks if character is uppercase
            amountUppercase += 1 #adds one to list of uppercase characters
    if amountUppercase >= 2: #checks if there are 2 or more uppercase characters
        return string.upper() #returns string in uppercase
    else:
        return string #returns original string




print(stringUpper(string))


def caesarCipher(string, shift):
    '''simple caesar cipher'''
    result = ""
    string = string
    for i in range(0,len(string)):
        char = string[i]

        if char == " ":
            result += " "

        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

encode = caesarCipher(string, 26)
decode = caesarCipher(string, 23)
print(encode, decode)
