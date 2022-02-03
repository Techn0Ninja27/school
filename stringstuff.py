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
    result = "" #creates string for storing encrypted output
    for i in range(0,len(string)): #loops for the length of the string
        char = string[i] # obtains single character

        #if character is uppercase
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
            # ord() changes character into integer for its unicode value
            # + shift adds the shift to the unicode value
            # - 65 makes all characters be ordered alphabetically
            # eg. E has a value of 45 in unicode HEX, but its integer value is
            # 69, subtracting 65 from 69 returns 4, which is the position of # -*- coding: utf-8 -*-
            # in the alphabet if counting from 0
            #
            # using the %(modulus) operator then makes the number not go over 26
            # eg 28 % 26 returns 2, and 5 % 26 returns 5
            # + 65 then makes the character go back to its original unicode value
            # chr() then takes an integer and returns a character from unicode
        #if character is lowercase
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

encode = caesarCipher(string, 26)
decode = caesarCipher(string, 23)
print(encode, decode)
