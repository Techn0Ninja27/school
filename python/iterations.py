# iterations

# while loop

def int_input(message, errorMessage="Input Error"):
    '''takes integer input from user'''
    inputFailure = True  # check for failure, default True
    while inputFailure:
        try:
            value = int(input(message))
        except ValueError:
            print(errorMessage)
        else:
            break
    return value



# for loop


def two_powers(n):
    '''prints powers of 2 until n'''
    for i in range(0, n):
        print(2 ** (i + 1))




# repeat probs

def repeat_two_powers():
    '''repeats two power function'''
    loopContinue = True
    while loopContinue:
        number = int_input("powers of two until", errorMessage="integer pls")
        print(f"powers of 2 until: {number}")
        two_powers(number)
        print()
        userInput = input("would you like to play again")
        if userInput == "y":
            continue
        else:
            loopContinue = False
            break

repeat_two_powers()
