# iterations

# while loop

def int_input(message, errorMessage="Input Error"):
    '''takes integer input from user'''
    inputFailure = True  # check for failure, default True
    while inputFailure:  # while loop that only stops when an input is added
        try:  # try code
            value = int(input(message))
        except ValueError:  # excepts an error
            print(errorMessage)
        else:
            break
    return value


# for loop


def two_powers(n):
    '''prints powers of 2 until n'''
    for i in range(0, n):  # for loop
        print(2 ** (i + 1))


# repeat probs

def repeat_two_powers():
    '''repeats two power function'''
    loopContinue = True
    # this is basically a do while in python
    # the check is created first, then the loop runs
    while loopContinue:
        # an input for integer
        number = int_input("powers of two until", errorMessage="integer pls")
        # prints the number chosen by the user
        print(f"powers of 2 until: {number}")
        two_powers(number)  # two powers function
        print()
        userInput = input("would you like to play again")
        if userInput == "y":
            # continue skips the rest of the loop and jumps straight back to
            # the test expression of the loop
            continue  # i think this is whats meant by repeat, but not sure
        else:
            loopContinue = False
            break


repeat_two_powers()
