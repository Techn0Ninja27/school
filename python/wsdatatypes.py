

# 1
def rectangle(length, width):
    '''calculates area of rectangle'''
    area = length * width
    return area
# 1


def rectangleInput():
    '''user input for rectangles'''
    length = float(input("rectangle length"))
    width = float(input("rectangle width"))
    print(rectangle(length, width))

# 2


def triangle(base, height):
    '''calculates area of triangle'''
    area = base * height * 0.5
    return area

# 2


def triangleInput():
    '''user input for triangle'''
    base = float(input("triangle base"))
    height = float(input("triangle height"))
    print((triangle(base, height)))

# 3


def carDetails():
    '''takes user input about cars and outputs a single string'''
    carInfo = {}  # opens a dictionary
    # carInfo["example"] opens a new entry in the dictionary
    # = input() assigns the users value to the entry
    carInfo["make"] = input("Enter the make of your car")
    carInfo["engine"] = input("Enter the engine size of your car")
    carInfo["color"] = input("Enter the color of your car")
    carInfo["age"] = input("Enter the age of your car")
    # print command to combine information into singular line
    print("you have a", carInfo["make"], "its engine size is", carInfo["engine"],
          "the color is", carInfo["color"], "it is", carInfo["age"], "years old")
    return carInfo


carDetails()
