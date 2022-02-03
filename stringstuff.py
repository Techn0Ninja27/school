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
    for c in firstChars: #loop to save code
        if c.isupper(): #checks if character is uppercase
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
        # if character is space
        if char == " ":
            # adds space to encrypted data
            result += " "
        #if character is uppercase
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
            # ord() changes character into integer for its unicode value
            # + shift adds the shift to the unicode value
            # - 65 makes all characters be ordered alphabetically
            # eg. E has a value of 45 in unicode HEX, but its integer value is
            # 69, subtracting 65 from 69 returns 4, which is the position of the character e
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

def caesarDecipher(string, shift):
    '''decoder for caesar cipher'''
    decodeShift = 26 - shift # creates shift to reshift a full cycle
    decode = caesarCipher(string, decodeShift) # re-encrypts to decrypt
    return decode

shift = 4
encode = caesarCipher(string, shift)
decode = caesarDecipher(encode, shift)
print(encode, "shift:", shift, decode)


def countRepeat(string):
    '''counts repeated characters in a string, returns dictionary'''
    chars = {} # opens dictionary to store characters
    for c in string: # iters through string
        if c in chars: # checks if key exists in dictionary
            chars[c] += 1 # if key exists then adds 1 to it
        else:
            chars[c] = 1 # if key does not exit then creates key
    repeatChars = {} # opens dictionary to store repeated characters
    for i in chars: # iters character dict
        if chars[i] < 2:
            # if charcter only appears once, skip
            pass
        else:
            # if the character repeats multiple times,
            # it will be added to the repeatedChars dict
            repeatChars[i] = chars[i]
    for i in repeatChars: # iters through repeated characters
        print(i, repeatChars[i]) # prints repeated charcter and number of times it was repeated

countRepeat(string)

def strToList(string):
    '''converts string to list'''
    list = [] # opens list
    for i in string: # iters through string
        list.append(i) # appends to list
    return list

list = strToList(string)
print(list)
