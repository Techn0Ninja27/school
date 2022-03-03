# mean

def mean(list):
    '''returns mean of list of numbers'''
    length = len(list)
    sum = 0
    try:
        for i, number in enumerate(list):
            sum += int(number)
    except ValueError:
        return None
    else:
        return sum / length


numbers = [1, 3, 4, 5, 7, 10]
music = ["enter sandman", "tornado of souls", "shot in the dark"]

print(mean(numbers))
print(mean(music))

# second to min


def sec_to_min():
    '''second to min'''
    return lambda second: second / 60


minute = sec_to_min()

print(minute(360))

# product


def product():
    '''product of two numbers'''
    return lambda a, b: a * b


multiply = product()

print(multiply(5, 7))

# pints to liters


def pint_to_l():
    '''convert pints to liters'''
    return lambda pint: pint / 2.2


liter = pint_to_l()

print(liter(6.6))

# difference


def difference():
    '''returns difference of two numbers'''
    return lambda a, b: a - b


diff = difference()

print(diff(7, 5))
