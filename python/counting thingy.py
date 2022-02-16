









# function for counting temperatures over 100 days
def temp_count():
    '''Counts temperature over 100 days and prints '''
    total1 = 0 # count for days where temp is under 20
    total2 = 0 # count for days where temp is over 20
    for i in range(100): # loops 100 times
        temp = float(input("Temperature for day", i+1)) # input for temp
        if temp < 20: # checks if temp is under 20
            total1 += 1 # adds 1 to count
        else: # if temp is not under 20
            total2 += 1 # adds 1 to count2
    # prints counts of temps
    print("days under 20c:", total1)
    print("days over 20c:", total2)
