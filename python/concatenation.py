# 1 & 2 & 3
def printInfo():
    loopFinish = False  # checks for user error
    while loopFinish is False:  # looped until no error
        try:
            # code run while checking for errors
            name = str(input("Name:"))  # input string
            age = float(input("Age:"))  # input float
            year = int(input("Year:"))  # input integer
        except ValueError:
            # run if error is found
            print("input error")
            continue
        else:
            # if no error, breaks loop
            loopFinish = True
    print("your name is", name, "you are", age,
          "years old, you are in year", year)
