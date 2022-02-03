def ageCompare():
    loopFinish = False
    while loopFinish == False:
        try:
            userName1 = str(input("enter name for person 1"))
            userAge1 = int(input("enter age for person 1"))
            userName2 = str(input("enter name for person 2"))
            userAge2 = int(input("enter age for person 2"))
        except:
            print("input error")
            continue
        else:
            loopFinish = True
    if userAge1 > userAge2:
        print(userName1, "is older than", userName2)
    elif userAge1 < userAge2:
        print(userName2, "is older than", userName1)
    elif userAge1 == userAge2:
        print(userName1, "is the same age as", userName2)

ageCompare()
