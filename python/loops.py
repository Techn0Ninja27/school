# 1
def loopMessage(message, count):
    '''loops printing a message'''
    for n in range(1, count, 1):  # loop
        print(message)


# 2
def userLoop():
    loopFinish = False  # checks for user error
    while loopFinish is False:  # looped until no error
        try:
            # code run while checking for errors
            loopMessage(input("message to loop"), int(
                input("number of times to loop")))
        except:
            # run if error is found
            print("input error")
            continue
        else:
            # if no error, breaks loop
            loopFinish = True

# 3


def timestable():
    '''timestable generator'''
    loopFinish = False  # user error prevention
    while loopFinish is False:  # loops to prevent user error
        try:
            # check for error
            times = int(input("enter times table you want"))
            limit = int(input("enter upper limit"))
        except ValueError:
            # if error
            print("input error")
            continue
        else:
            # breaks error loop
            loopFinish = True
    for i in range(1, limit+1):  # loop for code
        print(times, "*", i, "=", (times*i))  # prints the times table
