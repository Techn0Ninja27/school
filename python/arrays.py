import random

list = ["Master of Puppets", "21 Guns", "Shot in the Dark", "Chop Suey!",
        "Californication", "Wherever I May Roam", "Holiday", "Tornado Of Souls",
        "BYOB", "Master of Puppets"]

list2 = ["In Da Club", "Stan", "The Real Slim Shady", "Candy Shop"]

numbers = [69, 420, 666, 27]

emptyList = []

print(list)
print(list2)
print(numbers)
print(emptyList)

# 1


def listSum(list):
    '''sum of list'''
    sum = 0  # opens sum
    for i in list:  # iters through list
        sum += i  # adds to sum
    return sum


print(listSum(numbers))

# 2


def listProduct(list):
    '''product of list'''
    product = list[0]  # takes first entry of list
    for i in range(1, len(list)):  # iters through rest of list
        product *= list[i]  # multiplies product and list item
    return product


print(listProduct(numbers))

# 3 & 4


def listLowest(list, reverse=False):
    '''returns lowest value in list, if revese returns highest'''
    if reverse == True:  # if reverse
        list.sort(reverse=True)  # sorts list in reverse
    else:  # regular
        list.sort()  # sorts list
    return list[0]


print(listLowest(list))
print(listLowest(list, reverse=True))

# 5


def listStringThing(list):
    '''its a thing that does string'''
    count = 0  # starts count
    for i in list:  # iters through list
        string = str(i)  # makes all entries strings
        if len(string) >= 2:  # checks length of string
            if string[0] == string[-1]:  # checks if first and last char are the same
                count += 1  # adds to count
            else:
                pass
        else:
            pass
    return count


print(listStringThing(list))

# 6


def dupeRemove(list):
    '''removes duplicates from list'''
    output = []  # list for output list
    for i in list:  # iters through list
        if i not in output:  # checks if list item has already been added to output
            output.append(i)  # adds list item to output
        else:
            pass
    return output


print(dupeRemove(list))

# 8


def emptyCheck(list):
    '''checks if list is empty'''
    if len(list) == 0:  # checks if length of list is 0
        return True
    else:
        return False


print(emptyCheck(emptyList))

# 9


def dupeList(list):
    '''returns list from list'''
    return list

# 10


def wordLengthFinder(list, length):
    '''returns strings in list longer than length'''
    longWords = []  # opens list
    for i in list:  # iterates inputted list
        if len(i) > length:  # checks strings to see if they are longer
            longWords.append(i)  # appends to output list
    return longWords


print(wordLengthFinder(list, 10))

# 11


def commonItem(list1, list2):
    '''check for common items between lists'''
    common = False  # creates default output
    for i in list1:  # iters list1
        for o in list2:  # iters list2
            if i == o:  # checks for matches
                common = True  # changes output to true
    return common


print(commonItem(list, list2))

# 12


def remove0245(list):
    '''removes 0th 2nd 4th 5th element from list'''
    list.pop(0)
    list.pop(2)
    list.pop(4)
    list.pop(5)
    return list


print(remove0245(list))

# 13


def array3D(x, y, z):
    '''Generates 3D Array'''
    arrayZ = []  # Opens Z axis of array
    for i in range(z):
        arrayZ.append("*")  # Fills Z axis
    arrayY = [arrayZ] * y  # Creates Y axis
    arrayX = [arrayY] * x  # Creates X axis
    return arrayX


print(array3D(3, 4, 6))

# 14


def removeEven(list):
    '''removes even numbers'''
    oddList = []  # opens output list
    for i in list:  # iters list
        if (i % 2) != 0:  # checks if number is even
            # checks by diving by 2 and seeing if there is a remainder
            # if remainder is 0, it is even
            # therefore it checks if the remainder
            # is not equal to 0
            oddList.append(i)
    return oddList


print(removeEven(numbers))

# 15


def listShuffle(list):
    '''shuffle list'''
    random.shuffle(list)  # shuffles list, returns
    return list


print(listShuffle(list))
