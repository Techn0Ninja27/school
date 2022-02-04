# 1 & 2
def ageCompare():
    '''compares two different ages'''
    loopFinish = False #check for user error
    while loopFinish == False: #keeps input loop running until correct input
        try: #runs code and checks for error
            userName1 = str(input("enter name for person 1"))
            userAge1 = int(input("enter age for person 1"))
            userName2 = str(input("enter name for person 2"))
            userAge2 = int(input("enter age for person 2"))
        except:
            # run if error
            print("input error")
            continue
        else:
            #breaks loop
            loopFinish = True
    if userAge1 > userAge2: #if the first age is higher than the second
        print(userName1, "is older than", userName2)
    elif userAge1 < userAge2: #vice versa
        print(userName2, "is older than", userName1)
    elif userAge1 == userAge2: #equal
        print(userName1, "is the same age as", userName2)

ageCompare()
