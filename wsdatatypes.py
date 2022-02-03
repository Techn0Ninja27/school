




def rectangle(length, width):
    area = length * width
    return area

def rectangleInput():
    length = float(input("rectangle length"))
    width = float(input("rectangle width"))
    print(rectangle(length, width))

def triangle(base, height):
    area = base * height * 0.5
    return area

def triangleInput():
    base = float(input("triangle base"))
    height = float(input("triangle height"))
    print((triangle(base, height)))


def carDetails():
    carInfo = {}
    carInfo["make"] = input("Enter the make of your car")
    carInfo["engine"] = input("Enter the engine size of your car")
    carInfo["color"] = input("Enter the color of your car")
    carInfo["age"] = input("Enter the age of your car")
    print("you have a", carInfo["make"], "its engine size is", carInfo["engine"], "the color is", carInfo["color"], "it is", carInfo["age"], "years old")
    return carInfo

carDetails()
