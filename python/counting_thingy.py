

class Temp:
    '''
    A Class to represent temperature over days

    ...
    Attributes
    ----------
    days : int
        Amount of days to count temperature
    total1 : int
        count for temps under 20
    total2 : int
        count for temps above 20

    Methods
    -------
    tempcount()
        Takes user input for temperature over specified days
    __str__()
        Outputs string containing temperature info
    '''

    def __init__(self, days):

        self.days = days  # amount of days

        # counts for temps
        self.total1 = 0
        self.total2 = 0

    def temp_count(self):
        '''Counts temperature over specified days and prints '''
        total1 = 0  # count for days where temp is under 20
        total2 = 0  # count for days where temp is over 20
        for i in range(self.days):  # loops 100 times
            temp = float(input(f"Temperature for day {i+1}"))  # input for temp
            if temp <= 20:  # checks if temp is under 20
                self.total1 += 1  # adds 1 to count
            else:  # if temp is not under 20
                self.total2 += 1  # adds 1 to count2
        # prints counts of temps
        print("days under 20c:", self.total1)
        print("days over 20c:", self.total2)

    def __str__(self):
        '''Outputs message with string'''
        # uses fstrings, {} indicates variables
        message = f"Days under 20c: {self.total1}, Days over 20c: {self.total2}"
        return message


DayTemp = Temp(5)
DayTemp.temp_count()
print(DayTemp)


# function for counting temperatures over 100 days
def temp_count():
    '''Counts temperature over 100 days and prints '''
    total1 = 0  # count for days where temp is under 20
    total2 = 0  # count for days where temp is over 20
    for i in range(100):  # loops 100 times
        temp = float(input(f"Temperature for day {i+1}"))  # input for temp
        if temp <= 20:  # checks if temp is under 20
            total1 += 1  # adds 1 to count
        else:  # if temp is not under 20
            total2 += 1  # adds 1 to count2
    # prints counts of temps
    print("days under 20c:", total1)
    print("days over 20c:", total2)


temp_count()
